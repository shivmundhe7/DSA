
def rotateArr(arr, d):
    n = len(arr)
  
    
    for _ in range(d):
      
        
        last = arr[n - 1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2

    rotateArr(arr, d)

    
    for i in range(len(arr)):
        print(arr[i], end=" ")