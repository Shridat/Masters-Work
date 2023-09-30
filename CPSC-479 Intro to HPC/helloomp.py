from mpi4py import MPI
import os
import threading

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    processor_name = MPI.Get_processor_name()

    def worker():
        thread_id = threading.get_ident()
        nthreads = threading.active_count()
        print(f"Thread number {thread_id} (on {nthreads}) for the MPI process number {rank} (on {size}) [{processor_name}]")

    num_threads = 4
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    worker()

if __name__ == "__main__":
    main()