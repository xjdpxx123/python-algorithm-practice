a,b,c,d = map(int,input().split())

# hour = c - a
# minute = d - b
# if minute < 0:
#     minute += 60
#     hour -= 1

# print(hour,minute)

time = c * 60 + d - (a * 60 + b)

print(time // 60, time % 60)