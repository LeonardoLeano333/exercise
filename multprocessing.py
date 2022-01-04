import os
from multiprocessing import Pool

import random
import time

class PoolRunner(object):
    def __init__(self):
        self.processes = os.cpu_count()-1

    def runner(self, func_list):
        with Pool(self.processes) as p:
            procs = []
            # register the processes
            for func, args in func_list:
                proc = p.apply_async(func, args)
                procs.append(proc)
            
            # run every process in parallel
            for proc in procs:
                proc.get()
        return procs

def sleep_print(wait_time, value, start):
    time.sleep(wait_time)
    finish = time.time()
    print(finish-start)
    print(value)

if __name__ == '__main__':
    start = time.time()
    func_list = [
        (sleep_print,(1,"a",start)),
        (sleep_print,(2,"b",start)),
        (sleep_print,(4,"c",start)),
        (sleep_print,(8,"d",start))
    ]
    PoolRunner().runner(func_list)
