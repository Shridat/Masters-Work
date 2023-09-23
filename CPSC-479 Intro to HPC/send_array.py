from mpi4py import MPI 
import numpy as np

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    duration = 0
    A = np.zeros(2,dtype=np.int)
    B = np.zeros(2,dtype=np.int)
    start = MPI.Wtime()
    if rank == 0:
        A[0] = 1
        A[1] =34
        #comm.Send(A,dest=1)
        comm.Isend(A,dest=1)
        print(f"Process {rank} has sent the values of {A[0]}")
        print(f"Process {rank} has sent the values of {A[1]}")
    elif rank==1:
        #comm.Recv(B,source=0)
        recv_req = comm.Irecv(B,source=0)
        recv_req.Wait()
        end = MPI.Wtime()
        print(f"Process {rank} has recieve the values of {B[0]} and {B[1]}")
        print("Duration = ",end-start)

if __name__ == "__main__":
    main()