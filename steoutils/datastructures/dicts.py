def groupBys(iterable, keyers, valuer=lambda x: x):
    '''
        Given an iterable over objects of type U,
        a *list* of keyer functions [k0,k1,...]
            each of type U -> ki(U), hashable,
        and a veluer function U -> V(U),
        the (flat) iterable is made into a recursive map
            k0 -> k1 -> ... -> V(U)
        that is,
            {
                k0_a: {
                    k1_a: {
                        ...
                            ...
                                U
                    }
                }
    '''
    if len(keyers)==0:
        return [
            valuer(itm)
            for itm in iterable
        ]
    else:
        return {
            tK: groupBys(
                tVals,
                keyers=keyers[1:],
                valuer=valuer,
            )
            for tK,tVals in groupBy(
                iterable,
                keyer=keyers[0],
                valuer=lambda itm:itm,
            ).items()
        }

def groupBy(iterable, keyer, valuer=lambda x:x, callback=None,
            callbackFreq=1):
    '''
        Browses an iterable and groups the result of applying valuer to
        each item into lists, one per each distinct value of keyer(item)

        A callback may be provided, which must accept the number of items
        browsed and a callback calling frequency may also be passed
    '''
    dictionary = {}
    done = 0
    for item in iterable:
        key = keyer(item)
        if key not in dictionary:
            dictionary[key] = [valuer(item)]
        else:
            dictionary[key].append(valuer(item))
        done += 1
        if callbackFreq is not None and done % callbackFreq == 0 and callable(callback):
            callback(done)
    return dictionary
