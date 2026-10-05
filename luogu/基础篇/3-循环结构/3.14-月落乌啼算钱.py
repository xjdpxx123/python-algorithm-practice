# n = int(input())
#
# Fn = (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / 5 ** 0.5
#
# print(f"{Fn:.2f}")

# 这个题需要用到循环吗？？？
# 难道使用斐波那契数列的定义？
n = int(input())

a = 0
b = 1

for _ in range(n):
    a, b = b, a + b

print(f"{a:.2f}")