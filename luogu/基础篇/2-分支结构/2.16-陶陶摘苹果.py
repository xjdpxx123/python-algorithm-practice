a,b,c,d,e,f,g,h,i,j = map(int, input().split())
k = int(input())

num = 0

if a <= k+30:
    num += 1
if b <= k+30:
    num += 1
if c <= k+30:
    num += 1
if d <= k+30:
    num += 1
if e <= k+30:
    num += 1
if f <= k+30:
    num += 1
if g <= k+30:
    num += 1
if h <= k+30:
    num += 1
if i <= k+30:
    num += 1
if j <= k+30:
    num += 1

print(num)
