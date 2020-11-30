def main():
    for m in range(2, 100):
        
        for n in range(1, 100):
            if n >= m:
                break
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if a + b + c == 1000:
                print(a * b * c)
                return
    

main()