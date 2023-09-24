from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    token = 23
    start = MPI.Wtime()
    if rank==0:
        comm.send(token,dest = rank+1)
        #print(f"The process 0 has sent a token {token} to process 1")
        comm.recv(source=(rank-1)%size)
        end = MPI.Wtime()
        print("Elapsed time in Ring = ",end-start)
    else:
        comm.recv(source=(rank-1))
        #print(f"process {rank} has recieved token {token} from process {(rank-1)%size}")
        comm.send(token,dest = (rank+1)%size)
        #print(f"process {rank} has send token {token} to process {(rank+1)%size}")
    MPI.Finalize()
if __name__ == "__main__":
    main()