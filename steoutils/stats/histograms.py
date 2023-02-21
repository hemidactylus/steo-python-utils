import numpy as np

def makeHistogram(values, nBins, hRange=None, normalizeBars=False):
    '''
        returns a structure
            {
                'xs': [centres],
                'ys': [bar heights],
                'nSamples': integer,
                'width': float (step in the x values),
            }

        hRange, if passed, is a 2-tuple of boundary values
    '''
    _values = list(values)
    if hRange is not None:
        _y,_x = np.histogram(_values, bins=nBins, range=hRange)
    else:
        _y,_x = np.histogram(_values, bins=nBins)
    _x = 0.5*(_x[1:]+_x[:-1])
    #
    if normalizeBars:
        _sum = sum(_y)
        normer = float((_sum)*(_x[1]-_x[0]))
        if normer != 0:
            _y = [yy/normer for yy in _y]
    #
    return {
        'xs': _x,
        'ys': _y,
        'nSamples': len(_values),
        'width': _x[1]-_x[0],
    }
