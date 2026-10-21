N = int(input())

scores = []

# 保存所有同学的成绩
for i in range(N):
    chinese, mathematics, english = map(int, input().split())
    scores.append([chinese, mathematics, english])

count = 0

# 两两比较
for i in range(N):
    for j in range(i + 1, N):

        a = scores[i]
        b = scores[j]

        if (abs(a[0] - b[0]) <= 5 and abs(a[1] - b[1]) <= 5 and abs(a[2] - b[2]) <= 5 and abs(sum(a) - sum(b)) <= 10):

            count += 1

print(count)