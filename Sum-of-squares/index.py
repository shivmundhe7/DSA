def sumnum(n):
    return sum([i**2 for i in 
                range (1,n + 1)])
if __name__=="__main__":
    n = 2
    print(sumnum(n))