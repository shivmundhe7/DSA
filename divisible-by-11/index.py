def divBy11(s):
    
    n = int(s)
    return n % 11 == 0

if __name__ == "__main__":
    s = "76945"

    if divBy11(s):
        print("true")
    else:
        print("false")