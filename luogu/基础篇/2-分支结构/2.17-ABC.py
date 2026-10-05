x, y, z = map(int, input().split())
order = input()

# 将 x、y、z 排成从小到大
if x > y:
    x, y = y, x

if x > z:
    x, z = z, x

if y > z:
    y, z = z, y

# 此时：x 是最小值，y 是中间值，z 是最大值
if order == "ABC":
    print(x, y, z)
elif order == "ACB":
    print(x, z, y)
elif order == "BAC":
    print(y, x, z)
elif order == "BCA":
    print(y, z, x)
elif order == "CAB":
    print(z, x, y)
elif order == "CBA":
    print(z, y, x)