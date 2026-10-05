x = int(input())

flag0 = 0
flag1 = 0

if x % 2 == 0:
    flag0 = 1

if 4 < x <= 12:
    flag1 = 1

# 小 A：两个性质同时满足
if flag0 and flag1:
    print(1, end=' ')
else:
    print(0, end=' ')

# Uim：至少满足一个性质
if flag0 or flag1:
    print(1, end=' ')
else:
    print(0, end=' ')

# 小 B：刚好满足一个性质
if (flag0 == 1 and flag1 == 0) or (flag0 == 0 and flag1 == 1):
    print(1, end=' ')
else:
    print(0, end=' ')

# 正妹：两个性质都不满足
if flag0 == 0 and flag1 == 0:
    print(1)
else:
    print(0)