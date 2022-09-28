# 使用Taichi加速
import taichi as ti
import time
ti.init(arch=ti.cpu)
@ti.func
def is_prime(n: int):
    result = True
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            result = False
            break
    return result

@ti.kernel
def count_primes(n: int) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k):
            count += 1

    return count

time_start = time.time()
print(count_primes(1000000))
time_end = time.time()
print(time_end - time_start)
