n = int(input())

num = 1

# 控制行数
for i in range(1, n + 1):
    # 控制每一行的个数, 第 i 行的数字个数是 n−i+1
    for j in range(1, n - i + 2):
        if num < 10:
            print("0" + str(num), end="")
        else:
            print(num, end="")

        num += 1 # 计数器加 1
    
    print()

