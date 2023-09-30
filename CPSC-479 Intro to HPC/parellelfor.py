import numpy as np
from numba import jit,prange
N = 10000

@jit(parallel=True)
def main():
    a = np.empty(N, dtype=np.float64)
    b = np.empty(N, dtype=np.float64)
    c = np.empty(N, dtype=np.float64)

    for i in range(N):
        a[i] = i*2.0
        b [i] = i*3.0
    
    for i in prange(N):
        c[i] = a[i]+b[i]
    print(c[10])

if __name__ == '__main__':
    main() 

