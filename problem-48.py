def main():
    sum = 0
    for i in range(1, 1000+1):
        sum += i ** i
    print(str(sum)[-10:])

main()