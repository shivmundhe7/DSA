def findUnique(arr):
    n = len(arr)

    for i in range(n):

        count = 0

        for j in range(n):

            if arr[i] == arr[j]:
                count += 1

        if count == 1:
            return arr[i]

    return -1

if __name__ == "__main__":
    arr = [2, 3, 5, 4, 5, 3, 4]
    print(findUnique(arr))