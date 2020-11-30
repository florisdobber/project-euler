# Upper bound is    2177280 -> 7 * 9!
# That is less than 9999999, and so no number above that is valid

import math

def main():
    nums = []
    for i in range(3, 2177280+1):
        factorial_sum = sum(math.factorial(int(n)) for n in str(i))
        if factorial_sum == i:
            nums.append(i)
    print(sum(nums))


main()