n = int(input())

is_first = True
last_number = 0       # 上一个数
current_length = 0    # 当前这段连号的长度
max_length = 0        # 最长连号的长度

for number in map(int, input().split()):
    if is_first:
        # 保存第一个数
        last_number = number
        current_length = 1
        max_length = 1
        is_first = False
    else:
        # 当前数是否正好比上一个数大 1
        if number == last_number + 1:
            current_length += 1
        else:
            current_length = 1

        # 保存目前出现过的最长长度
        if current_length > max_length:
            max_length = current_length

        # 把当前数保存为“上一个数”
        last_number = number

print(max_length)