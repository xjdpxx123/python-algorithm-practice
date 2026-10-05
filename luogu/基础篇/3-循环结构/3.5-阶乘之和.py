n = int(input())

S = 0

# 阶乘累加
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    S += factorial

print(S)