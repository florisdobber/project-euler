import math

def main():
    num = math.factorial(100)
    num_str = str(num)
    sum = 0
    for n in num_str:
        sum += int(n)
    print(sum)

main()