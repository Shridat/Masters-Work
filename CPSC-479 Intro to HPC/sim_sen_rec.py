from mpi4py import MPI
import numpy as np
def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    print(f"I am {rank} of {size}")

    number = -1
    if rank ==0:
        comm.Send(np.array([number],dtype=np.int32),dest=1)
        print(f"Process 0 sent a number {number} to process 1")
    else:
        comm.Recv(np.empty(1,dtype=np.int32),source=0)
        print("process 1 recieved a number {number} from process 0")
    print(f"process{rank} has number {number}")

if __name__ == "__main__":
    main()