def main():
    count = 0
    i = 2
    while True:
        if is_prime(i):
            count += 1
        if count == 10001:
            break
        i += 1
    print(i)
    print(count)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

main()