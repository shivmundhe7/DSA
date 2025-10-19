import math

def buildSparseTable(arr):
    n = len(arr)

    lookup = [[0] * (int(math.log(n, 2)) + 1) for _ in range(n + 1)]

    for i in range(n):
        lookup[i][0] = arr[i]

    for j in range(1, int(math.log(n, 2)) + 1):

        for i in range(0, n - (1 << j) + 1):

            if lookup[i][j - 1] < lookup[i + (1 << (j - 1))][j - 1]:
                lookup[i][j] = lookup[i][j - 1]
            else:
                lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]

    return lookup

def query(L, R, lookup):

    j = int(math.log(R - L + 1, 2))

    if lookup[L][j] <= lookup[R - (1 << j) + 1][j]:
        return lookup[L][j]
    else:
        return lookup[R - (1 << j) + 1][j]

def solveQueries(arr, queries):
    n = len(arr)
    m = len(queries)
    result = [0] * m
    
    lookup = buildSparseTable(arr)
    
    for i in range(m):
        L = queries[i][0]
        R = queries[i][1]
        result[i] = query(L, R, lookup)
    
    return result

if __name__ == "__main__":
    arr = [ 7, 2, 3, 0, 5, 10, 3, 12, 18 ]
    queries = [ [0, 4], [4, 7], [7, 8] ]
    res = solveQueries(arr, queries)
    for x in res:
        print(x, end=" ")