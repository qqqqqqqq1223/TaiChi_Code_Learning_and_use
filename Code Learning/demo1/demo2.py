## 测试使用Taichi加速的效果
"""Count the prime numbers in the range [1, n]
"""

# Checks if a positive integer is a prime number
def is_prime(n: int):
    result = True
    # Traverses the range between 2 and sqrt(n)
    # - Returns False if n can be divided by one of them;
    # - otherwise, returns True
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            result = False
            break
    return result

# Traverses the range between 2 and n
# Counts the primes according to the return of is_prime()
def count_primes(n: int) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k):
           count += 1

    return count

print(count_primes(1000000))