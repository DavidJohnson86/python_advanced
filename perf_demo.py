import random
import time
from functools import wraps
from memory_profiler import profile
ESIZE=5_000_00

def measure(fn):
    @wraps(fn)
    def measure_runtime(*args, **kwargs):
        start_t = time.time()
        res = fn(*args, **kwargs)
        stop_t = time.time()
        print("Elapsed ({}): {} s".format(fn.__name__, stop_t-start_t))
        return res
    return measure_runtime

@measure
def generate_data():
    a=[]
    for i in range(ESIZE):
        #a.insert(0, random.random())
        a.append(random.random())
        #
    return a

@measure
def sum_mul(a, b):
    retval = 0
    for e1, e2 in zip(a, b):
        retval += e1 * e2
    return retval/ESIZE

def main():
    a = tuple(generate_data())
    b = tuple(generate_data())
    r = sum_mul(a, b)
    r2 = sum_mul(a, b)
    r3 = sum_mul(a, b)
    print(r)

if __name__ == "__main__":
    main()
