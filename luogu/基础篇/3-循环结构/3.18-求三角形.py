n = int(input())

for i in range(n):
    for j in range(n):
        num = i * n + j + 1

        if num < 10:
            print("0" + str(num), end="")
        else:
            print(num, end="")

    print()

print()

num = 1

# 控制行数
for i in range(1, n + 1):

    # 每行前面的空格
    for k in range(n - i):
        print("  ", end="")

    # 第 i 行打印 i 个数字
    for j in range(1, i + 1):
        if num < 10:
            print("0" + str(num), end="")
        else:
            print(num, end="")

        num += 1

    print()