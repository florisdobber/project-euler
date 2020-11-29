def main():
    number = 600851475143
    prime_list = []
    while True:
        factor = smallest_prime(number)
        if factor == number:
            prime_list.append(factor)
            break
        number = int(number / factor)
        prime_list.append(factor)
    print(max(prime_list))

def smallest_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


main()