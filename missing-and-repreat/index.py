def findTwoElement(arr):
    n = len(arr)

    freq = [0] * (n + 1)
    repeating = -1
    missing = -1

    for num in arr:
        freq[num] += 1

    for i in range(1, n + 1):
        if freq[i] == 0:
            missing = i
        elif freq[i] == 2:
            repeating = i

    return [repeating, missing]

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)
    print(ans[0], ans[1])