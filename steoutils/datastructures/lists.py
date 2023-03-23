def uniquify(lst,key=lambda itm: itm):
    '''
        skips already-inserted items and returns
        a new, possibly shorter list.

        This is a generalised delete_duplicates, in that it allows
        to work on a list of non-hashable items [A1,A2,A3...]
        and the uniqueness acts on a generic key function
            key: A -> K       (K must be hashable)
        so that the resulting list guarantees unicity of
        the key applied to the surviving elements
    '''
    newL = []
    usedKeys = set()
    for itm in lst:
        itmKey=key(itm)
        if itmKey not in usedKeys:
            newL.append(itm)
            usedKeys.add(itmKey)
    return newL
