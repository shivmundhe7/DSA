def count_pairs(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(n + 1):
            if a**3 + b**3 == n:
                count += 1
    return count

n = 9
print(count_pairs(n))