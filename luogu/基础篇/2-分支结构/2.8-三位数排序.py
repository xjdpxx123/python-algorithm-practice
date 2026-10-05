a,b,c = map(int, input().split())

# 排序，用分支语句
if a > b:
    if a > c:
        if b > c:
            print(c, b, a)
        else:
            print(b, c, a)
    else:
        print(b, a, c)
else:
    if b > c:
        if a > c:
            print(c, a, b)
        else:
            print(a, c, b)
    else:
        print(a, b, c)
