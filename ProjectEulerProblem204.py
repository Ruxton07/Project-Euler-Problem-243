'''A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?'''

def count_generalised_hamming_numbers(n, limit):
    count = 0
    for i in range(1, limit + 1):
        if is_generalised_hamming_number(i, n):
            count += 1
    return count

def is_generalised_hamming_number(num, n):
    for prime in range(2, n + 1):
        while num % prime == 0:
            num //= prime
    return num <= n

def main():
    n = 100
    limit = 10**9
    count = count_generalised_hamming_numbers(n, limit)
    print(f"There are {count} generalised Hamming numbers of type {n} which don't exceed {limit}.")
    
if __name__ == "__main__":
    main()