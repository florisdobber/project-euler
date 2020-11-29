def main():
    last = 1
    new = 1
    total = 0
    while True:
        if new > 4000000:
            break
        if new % 2 == 0:
            total += new
        new_copy = new
        new += last
        last = new_copy
    print(total)

main()