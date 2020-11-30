def main():
    sum = 0
    
    for i in range(1, 1000000+1):
        if is_palindrome(i) and is_palindrome(to_binary(i)):
            sum += i

    print(sum)

def to_binary(n):
    return bin(n).replace("0b", "")

def is_palindrome(num):
    num_str = str(num)
    reverse = num_str[::-1]
    return num_str == reverse

main()