import re
import time

def some_function(a, b):
    t1 = time.time()
    c = a + b
    print("time cost:", time.time()-t1)
    return c

print(some_function(3, 4))

def sb_func(x, y, z):
    print("I'm SB!!!!!!")

def main(a, b, c):
    return some_function(a, b) + c

if __name__ == "__main__":
    sb_func("d", "s", "b")
    main(1, 2, 3)
