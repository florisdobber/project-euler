def main():
    sum = 0
    limit = 1000
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)

main()