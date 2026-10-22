n = int(input())

magic_square = []

magic_square = [[0] * n for _ in range(n)]

# 把 1 放在第一行中间
row = 0
col = n // 2

magic_square[row][col] = 1

# 从 2 开始填写
for num in range(2, n * n + 1):

    if row == 0 and col != n - 1:
        row = n - 1
        col += 1

    elif col == n - 1 and row != 0:
        row -= 1
        col = 0

    elif row == 0 and col == n - 1:
        row += 1

    else:
        if magic_square[row - 1][col + 1] == 0:
            row -= 1
            col += 1
        else:
            row += 1

    magic_square[row][col] = num

# 输出二维数组
for i in range(n):
    for j in range(n):
        print(magic_square[i][j], end=" ")
    print()