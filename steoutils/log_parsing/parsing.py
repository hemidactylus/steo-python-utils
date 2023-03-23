def cut_blocks(line_stream, matcher, separator_mode, keep_remainder=False):
    # separator_mode = 'start_match' / 'end_match'
    blocks = []
    buffer = []
    #
    if separator_mode == 'start_match':
        matches_found = False
        for _line in line_stream:
            line = _line.replace('\n', '')
            if matcher(line):
                if buffer:
                    if matches_found or keep_remainder:
                        blocks += [buffer]
                    buffer = []
                buffer = [line]
                matches_found = True
            else:
                buffer += [line]
        # handle last block
        if buffer:
            blocks += [buffer]
            buffer = []
    elif separator_mode == 'end_match':
        for _line in line_stream:
            line = _line.replace('\n', '')
            if matcher(line):
                buffer += [line]
                blocks += [buffer]
                buffer = []
            else:
                buffer += [line]
        # handle last block
        if buffer and keep_remainder:
            blocks += [buffer]
            buffer = []
    else:
        raise ValueError('unknown separator_mode')
    #
    return blocks



def parse_log(line_stream, start_matcher=None, end_matcher=None, keep_remainder=False, block_parser=lambda bl: bl, title=None):
    if title:
        print(f'Parsing {title}')
    if start_matcher:
        blocks = cut_blocks(line_stream, start_matcher, separator_mode='start_match', keep_remainder=keep_remainder)
    elif end_matcher:
        blocks = cut_blocks(line_stream, end_matcher, separator_mode='end_match', keep_remainder=keep_remainder)
    else:
        raise ValueError('unspecified line matchers')
    #
    return [block_parser(bl) for bl in blocks]
