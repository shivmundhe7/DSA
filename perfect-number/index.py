def isPerfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

if __name__ == '__main__':
    n = 15
    print("true" if isPerfect(n) else "false")