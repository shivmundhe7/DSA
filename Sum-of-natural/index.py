def Findsum(n):
    sum = 0
    x = 1
    
    while x <= n:
        sum = sum + x
        x = x + 1
    return sum

if __name__=="__main__":
    n = 8
    print(Findsum(n))