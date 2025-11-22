# Python program to find the digit sum 
# using mathematical formula

def singleDigit(n):
  
    # If given number is zero its
    # digit sum will be zero only
    if n == 0: 
        return 0
    
    # If result of modulo operation is 
    # zero then, the digit sum is 9
    if n % 9 == 0:
        return 9
    
    return n % 9

if __name__ == "__main__":
    n = 1234
    print(singleDigit(n))