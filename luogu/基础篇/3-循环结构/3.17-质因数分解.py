"""超时了！！！"""
# n = int(input())
#
# p = 2
#
# i = 3
#
# while i < n:
#     if n % i == 0 and i > p:
#         p = i
#     i += 2
#
# print(p)

"""优化"""
n = int(input())

p = n // 2      # 如果较小质数是 2，这就是答案

i = 3

while i * i <= n:       # 只检查到平方根
    if n % i == 0:
        p = n // i      # i 是较小质数，n // i 是较大质数
        break           # 找到后立即结束

    i += 2

print(p)