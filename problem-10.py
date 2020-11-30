import math

def main():
    numbers_list = enumerate(list_of_primes(2000000))
    primes_list = [prime for prime, boolean in numbers_list if boolean]
    print(sum(primes_list))

def list_of_primes(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False

	for i in range(int(math.sqrt(n) + 1)):

		if result[i]:
			
			for j in range(i * i, len(result), i):
				result[j] = False

	return result


main()