n = int(input())

s = 0
max = 0
min = 10

for x in map(int, input().split()):
    s += x
    if x > max:
        max = x
    if x < min:
        min = x

ans = (s - max - min) / (n - 2)
print("%.2f" % ans)