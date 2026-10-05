n = int(input())

max_number = -1
min_number = 1001

for number in map(int, input().split()):
    if number > max_number:
        max_number = number

    if number < min_number:
        min_number = number

print(max_number - min_number)