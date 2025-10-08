
def findSum(arr, start, end):
    sum_ = 0
    for i in range(start, end + 1):
        sum_ += arr[i]
    return sum_

def findSplit(arr):
    n = len(arr)
  
    for i in range(n - 2):
        
        for j in range(i + 1, n - 1):
            
            sum1 = findSum(arr, 0, i)
            sum2 = findSum(arr, i + 1, j)
            sum3 = findSum(arr, j + 1, n - 1)
            
            if sum1 == sum2 and sum2 == sum3:
                return [i, j]
  
    return [-1, -1]

if __name__ == "__main__":
    arr = [1, 3, 4, 0, 4]
    res = findSplit(arr)
    
    print(res[0], res[1])