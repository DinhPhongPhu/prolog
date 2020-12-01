class kmot:
    x = int()
    y= int()
def create_array_structs(_class,  _n):
    _as = list()
    for i in range(0,_n):
        for j in range(0,_n):
            _as.append(_class())
    return _as
def maxLengthOfBits(arr):
    n = len(arr)
    if (n < 2): return 0
    t=create_array_structs(km,n)
    for i in range (0,n):
        for j in range (0,n):
            t[i][j].x = 0
            t[i][j].y = 0

    if (arr[0] == 1): t[0][0].x+=1
    else: t[0][0].y+=1
    for i in range (1,n):
        for j in range (0,i+1):
            if (arr[i] == 1):
                t[j][i].x = t[j][i - 1].x + 1
                t[j][i].y = t[j][i - 1].y
            if (arr[i] == 0):
                t[j][i].y = t[j][i - 1].y + 1
                t[j][i].x = t[j][i - 1].x
    max = 0
    for i in range (0,n):
        for j in range (0,n):
            if (t[i][j].x == t[i][j].y and t[i][j].x > max): max = t[i][j].x
    return max

p=[0,1,1,0]
print(maxLengthOfBits(p))