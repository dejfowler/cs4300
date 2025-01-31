#!/usr/bin/python3

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = 0
primes = []
while num < 10:
    start = 2
    while num < 10:
        if is_prime(start):
            primes.append(start)
            num += 1
        start += 1
print(primes)

i = 1
sum = 0
while i < 101:
    sum += i
    i += 1
print(sum)