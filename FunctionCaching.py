from time import time


import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some task")
    some_work(3)
    # some_work(4)
    print("Work in progress")
    some_work(3)
    print("Work completed")