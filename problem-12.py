import math

def main():
    next_num = 2
    current_sum = 1
    while True:
        result = num_divisors(current_sum)
        if result > 500:
            break
        current_sum += next_num
        next_num += 1
    print(current_sum)

def num_divisors(n):
    divisors = set()
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
        i += 1

    return len(divisors)


main()