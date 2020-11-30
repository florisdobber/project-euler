def main():
    n1 = 0
    n2 = 1
    count = 1

    while len(str(n2)) < 1000:
        n1_copy = n1
        n1 = n2
        n2 += n1_copy
        count += 1
    
    print(count)

main()
