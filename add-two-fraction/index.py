from math import gcd

def addFraction(a, b):
    den = gcd(a[1], b[1])

    den = (a[1] * b[1]) // den

    num = (a[0]) * (den // a[1]) + (b[0]) * (den // b[1])

    common_factor = gcd(num, den)

    den //= common_factor
    num //= common_factor
    return [num, den]

if __name__ == '__main__':
    a = [1, 2]
    b = [3, 2]
    ans = addFraction(a, b)
    print(f'{ans[0]}, {ans[1]}')