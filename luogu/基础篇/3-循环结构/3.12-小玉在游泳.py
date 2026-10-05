s = float(input())

first_step_length = 2
n = 2
total_step = 1
next_step_length= first_step_length

while n < s :
    next_step_length *= 0.98
    n += next_step_length
    total_step += 1

print(total_step)