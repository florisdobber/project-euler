def main():
    number = 20
    while True:
        if divisible_by_all(number):
            print(number)
            return
        else:
            if number % 1000 == 0:
                print(number)
            number += 20

def divisible_by_all(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    return True

main()