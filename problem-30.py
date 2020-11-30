# Limit is defined as 354294, or 9^5 + 9^5 + 9^5 + 9^5 + 9^5 + 9^5
# This is less than   999999, meaning that its fifth power sum could
# never be equal to anything above 

def main():
    nums = []
    for i in range(2, 354294):
        if i == sum_of_fifth_power(i):
            nums.append(i)
    print(sum(nums))
        

def sum_of_fifth_power(n):
    total = 0
    for i in str(n):
        total += int(i) ** 5
    return total

main()