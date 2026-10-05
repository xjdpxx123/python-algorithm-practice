a, b, c = map(int, input().split())

# 找三个数中的最小值
small = a

if b < small:
    small = b

if c < small:
    small = c

# 找三个数中的最大值
large = a

if b > large:
    large = b

if c > large:
    large = c


x = small
y = large

# 求最大公约数
while y != 0:
    remainder = x % y
    x = y
    y = remainder

gcd = x

# 分子和分母同时除以最大公约数
new_small = small // gcd # // int，/ float
new_large = large // gcd

print(str(new_small) + "/" + str(new_large))



# from math import gcd # 在不使用循环的条件下，需要使用内置函数解决，我没想到其它解决办法

# a, b, c = map(int, input().split())

# small = a

# if b < small:
#     small = b

# if c < small:
#     small = c

# large = a

# if b > large:
#     large = b

# if c > large:
#     large = c

# common_divisor = gcd(small, large)

# print(f"{small // common_divisor}/{large // common_divisor}")