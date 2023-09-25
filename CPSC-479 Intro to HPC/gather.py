from mpi4py import MPI

def main():
    n = 5
    b = 0
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    a = [0]*n
    b = rank
    print(f"Process of rank {rank} has array {a} and b = {b}")
    a = comm.gather(b,root=2)

    print(f"Process of rank {rank} has array {a} and b = {b}")

if __name__ == "__main__":
    main()


