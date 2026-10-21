n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    s = 0
    for j in range(i):
        if a[j] < a[i]:
            s += 1
    print(s, end=" ")