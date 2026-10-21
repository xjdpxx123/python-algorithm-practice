n = int(input())
a = [n]

while n != 1:
    if n % 2 == 1:
        n = n * 3 + 1
    else:
        n = n // 2
    a.append(n)

a.reverse()

for i in a:
    print(i, end=" ")