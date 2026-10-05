s,v = map(int, input().split())

walk_time = (s+v-1)//v # 适用于整数
# walk_time = s // v
# if s%v != 0:
#     walk_time += 1

total_time = walk_time + 10

leave_time = (8*60 - total_time) % (24*60)

hour = leave_time // 60
minute = leave_time % 60

print(f"{hour:02d}:{minute:02d}")