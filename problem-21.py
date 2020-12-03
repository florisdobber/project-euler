import math

def main():
    sum = 0
    for i in range(2, 10000):
        if i == proper_divisors_sum(proper_divisors_sum(i)) and i != proper_divisors_sum(i):
            sum += i
    print(sum)

def proper_divisors_sum(n):
    if n == 1:
        return 0
    divisors = [1]

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != math.sqrt(n):
                divisors.append(int(n / i))
    return sum(divisors)

main()