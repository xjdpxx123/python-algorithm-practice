n,k = map(int, input().split())

A_class = 0
num_A = 0
B_class = 0
num_B = 0

for i in range(1, n+1):
    if i % k == 0:
        A_class += i
        num_A += 1
    else:
        B_class += i
        num_B += 1

print(f"{A_class/num_A:.1f} {B_class/num_B:.1f}")

