# n = int(input())

# numbers = input().split()

# while len(numbers) != n:
#     print("输入数量不正确，请重新输入")
#     numbers = input().split()

# for i in range(n):
#     numbers[i] = int(numbers[i])

# min_value = 1001

# for i in range(n):
#     if numbers[i] < min_value:
#         min_value = numbers[i]

# print(min_value)

# 不使用数组/字符串知识点
n = int(input())

min_value = 1001

for number in map(int, input().split()):
    # 不管n
    if number < min_value:
        min_value = number

print(min_value)