h, r = map(int, input().split())

# v  = 3.14 * r * r * h / 1000
# t = int((20 + v - 1) // v)，只适用于整数，此题失效，需要调整成整数
v  = 314 * r * r * h
t = (20_00000 + v - 1) // v # 1_0 等价于 10

print(t)