# a = float(input())
# print(str(a)[::-1])

# 不使用字符串知识点
number = int(float(input()) * 10 + 0.5) # +0.5，防止浮点数精度问题

ones_after_decimal = number % 10
ones = number // 10 % 10
tens = number // 100 % 10
hundreds = number // 1000

print(ones_after_decimal, ".", ones, tens, hundreds, sep="")