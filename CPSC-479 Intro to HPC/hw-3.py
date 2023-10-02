from mpi4py import MPI
import random

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    #charging_times = [30,10,70,10,40,10,60,30]
    charging_time = random.randint(10,99)
    print(f"Chanrging time of process {rank} = {charging_time}")
    #total_time = sum(charging_times)
    cumulative_time = [0]*size
    cumulative_time[rank] = comm.scan(charging_time, op = MPI.SUM)
    #print(cumulative_time[rank])
    start = cumulative_time[rank]-charging_time
    end = cumulative_time[rank]
    hrs = cumulative_time[rank]//60
    mins = cumulative_time[rank]%60

    print(f"Rank {rank} will start charging after {start} minutes ({hrs} hours {mins} minutes) and will be done after {end} minutes")
    comm.Barrier()

if __name__ == "__main__":
    main()