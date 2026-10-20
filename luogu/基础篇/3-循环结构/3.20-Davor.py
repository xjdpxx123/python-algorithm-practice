n = int(input())

# 从最大的开始找（题目要求）
for x in range(100, 0, -1):
    # 从最小的开始找（题目要求）
    for k in range(1, 134):
        # 52(7X+21K)=364X+1092K
        if 364 * x + 1092 * k == n:
            print(x)
            print(k)
            break
    else:
        continue
    break