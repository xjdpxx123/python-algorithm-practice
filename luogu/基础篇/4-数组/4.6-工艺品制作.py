w, x, h = map(int, input().split())
q = int(input())

cuts = []

for _ in range(q):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    cuts.append((x1, y1, z1, x2, y2, z2))

# 创建三维数组
cube = []

for i in range(w):
    layer = []
    for j in range(x):
        row = [0] * h
        layer.append(row)
    cube.append(layer)

# 一开始所有小方块都存在
count = w * x * h

# 遍历每一次切割
for i in range(q):
    x1, y1, z1, x2, y2, z2 = cuts[i]

    for a in range(x1, x2 + 1):
        for b in range(y1, y2 + 1):
            for c in range(z1, z2 + 1):
                if cube[a - 1][b - 1][c - 1] == 0:
                    cube[a - 1][b - 1][c - 1] = 1
                    count -= 1

print(count)