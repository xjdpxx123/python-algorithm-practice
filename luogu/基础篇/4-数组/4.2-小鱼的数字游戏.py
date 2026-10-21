n = list(map(int, input().split()))

for i in range(1, len(n)):
    print(n[len(n) - 1 - i], end=" ")