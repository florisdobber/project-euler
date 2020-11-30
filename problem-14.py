def main():
    max_length = 0
    num = -1
    for i in range(1, 1000000+1):
        c_length = collatz_length(i)
        if c_length > max_length:
            max_length = c_length
            num = i
    print(num)

def collatz_length(n):
    length = 1
    while True:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1 
        length += 1
        if n == 1:
            break
    return length


main()