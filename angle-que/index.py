def getMin(x, y):
    return x if x < y else y

def getAngle(s):
    h = int(s[:2])
    m = int(s[3:])

    h = h % 12

    hrAngle = 0.5 * (h * 60 + m)

    minAngle = 6 * m

     angle = abs(hrAngle - minAngle)

    return getMin(360 - angle, angle)

if __name__ == "__main__":
    s = "06:00"
    print(f"{getAngle(s):.3f}")