from operator import itemgetter


def groupBys(iterable, keyers, valuer=lambda x: x):
    '''
        Given an iterable over objects of type U,
        a *list* of keyer functions [k0,k1,...]
            each of type U -> ki(U), hashable,
        and a valuer function U -> V(U),
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


def flipTwoLevelDict(dct):
    '''
        Assuming a homogeneous depth-2 dict
            k1 -> k2 -> v
        flip the key nesting and return a dict
            k2 -> k1 -> v
    '''
    return {
        gk1: {
            gk2: gvs[0]
            for gk2, gvs in gk2vs.items()
        }
        for gk1, gk2vs in groupBys(
            (
                (k1, k2, v)
                for k1, k2v in dct.items()
                for k2, v in k2v.items()
            ),
            keyers=[itemgetter(1), itemgetter(0)],
            valuer=itemgetter(2),
        ).items()
    }
