from mpi4py import MPI
import numpy as np

def block_single_tran(comm,send_buf,recv_buf,rank):
    end = 0
    elapsed = 0
    start = MPI.Wtime()
    if rank==0:
        comm.Send(send_buf,dest=1)
    elif rank==1:
        comm.Recv(recv_buf,source=0)
        end = MPI.Wtime()
        elapsed = end - start
        print(f"Blocking Communication - Single transmission = ",elapsed)

def non_block_single_tran(comm,send_buf,recv_buf,rank):
    end = 0
    elapsed = 0
    start = MPI.Wtime()
    if rank==0:
        comm.Isend(send_buf,dest=1)
        #req_send.wait()
    elif rank==1:
        req_recv = comm.Irecv(recv_buf,source=0)
        req_recv.wait()
        end = MPI.Wtime()
        elapsed = end - start
        print("Non-blocking single transmission = ", elapsed)

def block_roundtrip(comm,send_buf,recv_buf,rank):
    end = 0
    elapsed = 0
    start = MPI.Wtime()
    if rank==0:
        comm.Send(send_buf,dest=1)
        comm.Recv(recv_buf,source=1)
        end = MPI.Wtime()
        elapsed = end - start
        print("Blocking Communication- Round trip Transmission = ", elapsed)
    elif rank==1:
        comm.Recv(recv_buf,source=0)
        comm.Send(recv_buf,dest=0)
        
def non_block_roundtrip(comm,send_buf,recv_buf,rank):
    end = 0
    elapsed = 0
    start = MPI.Wtime()
    if rank==0:
        req_send = comm.Isend(send_buf,dest=1)
        req_recv = comm.Irecv(recv_buf,source=1)
        req_send.Wait()
        req_recv.Wait()
        end = MPI.Wtime()
        elapsed = end-start
        print("Non-blocking Communication - round trip time = ", elapsed)
    elif rank==1:
        req_recv = comm.Irecv(recv_buf,source=0)
        req_send = comm.Isend(send_buf,dest=0)
        req_recv.wait()
        req_send.wait()

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    string_len = 64
    send_buf = bytearray(string_len)
    recv_buf = bytearray(string_len)
    name = "Shrinivas"
    send_buf[:len(name)] = name.encode('utf-8')
    block_single_tran(comm,send_buf,recv_buf,rank)
    non_block_single_tran(comm,send_buf,recv_buf,rank)
    block_roundtrip(comm,send_buf,recv_buf,rank)
    non_block_roundtrip(comm,send_buf,recv_buf,rank)

if __name__ == "__main__":
    main()