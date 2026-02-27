import numpy as np

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish +1)
    out = np.array(numvec, dtype = object)

    n3 = (numvec % 3 ==0)
    n5 = (numvec % 5 ==0)

    out[n3] = "fizz"
    out[n5] = "buzz"
    out[n3 & n5] = "fizzbuzz"
    
    return (out)
