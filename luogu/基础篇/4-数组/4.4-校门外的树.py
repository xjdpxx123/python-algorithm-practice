l, m = map(int, input().split())

# 1. 创建列表，表示所有位置都有树
trees = [1] * (l + 1)

# 2. 输入每个需要移走树的区域
for i in range(m):
    u, v = map(int, input().split())

    # 3. 移走这个区域内的树
    for j in range(u, v + 1):
        trees[j] = 0

# 4. 统计剩下的树
print(sum(trees))