def main():
    number = 2 ** 1000
    num_str = str(number)
    sum = 0
    for n in num_str:
        sum += int(n)
    print(sum)

main()