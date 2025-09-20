# Iterate Python Program to print alternate elements
# of the array

def getAlternates(arr):
    res = []
    
    # Iterate over all alternate elements
    for i in range(0, len(arr), 2):
        res.append(arr[i])
    return res

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates(arr)
    print(" ".join(map(str, res)))