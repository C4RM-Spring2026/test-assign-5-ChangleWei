import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange (1, n + 1)
    discount = 1 / ((1 + r ) ** t)
    pv_coupons = np.sum(c * discount)
    pv_face = face * discount[-1]
    
    return(pv_coupons + pv_face)
