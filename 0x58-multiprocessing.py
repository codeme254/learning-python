#!/usr/bin/python3

# Python multiprocessing
# Running taks in parallel on different cpu cores, bypasses GIL used for threading.
# multiprocessing is better for heavy cpu usage
# multithreading is better for waiting around

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    # creating a process
    a = Process(target=counter, args=(500000000,))
    # starting the process.
    a.start()
    # process synchronization with join.
    # a.join()
    # print("finished in: ",time.perf_counter(), " seconds")
    # it takes close to 1 minute to finish counting the above, this can be made shorter using multiprocessing
    b = Process(target=counter, args=(500000000, ))
    b.start()
    a.join()
    b.join()
    print("finished in: ",time.perf_counter(), " seconds")

if __name__ == "__main__":
    main()
