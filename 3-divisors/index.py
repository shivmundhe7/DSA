# function to count number of divisors of n
def exactly3Divisors(n):
    count = 0
    for i in range(1, n+1):
        # number n is divisible by i 
        if n % i == 0:
            count += 1
    return count

# function to count numbers with 
# exactly 3 divisors up to n
def countDivisors(n):
    total = 0
    for i in range(1, n+1):
        if exactly3Divisors(i) == 3:
            total += 1
    return total
if __name__ == "__main__":
    n = 100
    ans = countDivisors(n)
    print(ans)