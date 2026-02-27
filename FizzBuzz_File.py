import numpy as np

def FizzBuzz(start, finish):
    n = np.arange(start, finish +1)
    out = []

    n3 = (n % 3 ==0)
    n5 = (n % 5 ==0)

    out[n3] = "fizz"
    out[n5] = "buzz"
    out[n3 & n5] = "fizzbuzz"
    out[n] = n
    
    return(out)
