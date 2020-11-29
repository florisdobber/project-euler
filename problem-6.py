def main():
    sum_squares = 0
    square_sum = 0
    for i in range(1, 101):
        sum_squares += i * i
        square_sum += i
    square_sum = square_sum ** 2
    print(square_sum - sum_squares)

main()