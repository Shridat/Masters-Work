from mpi4py import MPI
import numpy as np

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    b = 0
    n = 5
    #a = np.zeros(n,dtype=np.int)
    a = [0]*n
    print(f"The process {rank} has b before scatter = {b}")
    if rank==2:
        for i in range(n):
            a[i] = (i+1)**2
    b = comm.scatter(a,root=2)
    print(f"The process {rank} has b after scatter = {b}")

if __name__ == "__main__":
    main()
