import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = m * ppy
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange (1, n +1)
    discount = 1 / ((1 + r) ** t)

    cf = np.full (n, c)
    cf[-1] = cf[-1] + face

    pvcf = cf * discount
    pvcf_sum = np.sum(pvcf)

    ty = t / ppy
    duration = np.sum(ty * pvcf) / pvcf_sum
    return(duration)
