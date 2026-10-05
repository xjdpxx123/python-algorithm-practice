a, b, c = map(int, input().split())

# 判断是否能组成三角形
if a + b <= c or a + c <= b or b + c <= a:
    print("Not triangle")
else:
    # 判断角度类型
    if (a ** 2 + b ** 2 == c ** 2 or
        a ** 2 + c ** 2 == b ** 2 or
        b ** 2 + c ** 2 == a ** 2):
        print("Right triangle")

    elif (a ** 2 + b ** 2 > c ** 2 and
          a ** 2 + c ** 2 > b ** 2 and
          b ** 2 + c ** 2 > a ** 2):
        print("Acute triangle")

    else:
        print("Obtuse triangle")

    # 以下条件可能与角度类型同时成立，因此必须单独判断
    if a == b or a == c or b == c:
        print("Isosceles triangle")

    if a == b == c:
        print("Equilateral triangle")