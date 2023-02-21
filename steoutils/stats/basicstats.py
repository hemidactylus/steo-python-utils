import numpy as np

def getStats(valList):
    _valList = [vl for vl in valList if vl is not None]
    return {
        'mean': np.mean(_valList),
        'std': np.std(_valList),
        'max': np.max(_valList),
        'min': np.min(_valList),
    } if len(_valList) > 0 else {
        'mean': 0.0,
        'std':  0.0,
        'max':  0.0,
        'min':  0.0,
    }
