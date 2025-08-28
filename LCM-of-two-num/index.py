def lcm(a, b):
    

    g = max(a, b) 

    s = min(a, b)  

    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    return a * b 


if __name__ == '__main__':
    a = 10
    b = 5
    print(lcm(a, b))