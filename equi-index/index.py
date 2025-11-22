# Python program to find equilibrium index of an array
# using nested loop

def findEquilibrium(arr):
    
    # Check for indexes one by one until
    # an equilibrium index is found 
    for i in range(len(arr)):
        # Get left sum
        leftSum = sum(arr[:i])

        # Get right sum
        rightSum = sum(arr[i + 1:])

        # If leftsum and rightsum are same, then 
        # index i is an equilibrium index
        if leftSum == rightSum:
            return i

    # If equilibrium index doesn't exist
    return -1
  
if __name__ == '__main__':
    arr = [-7, 1, 5, 2, -4, 3, 0]

    print(findEquilibrium(arr))