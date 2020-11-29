def main():
    result = -1
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j):
                result = max(result, i * j)
    print(result)

def is_palindrome(num):
    num_str = str(num)
    reverse = num_str[::-1]
    return num_str == reverse

main()