n = int(input())

Local_time = 5*n
Luogu_time = 11 + 3*n

if Local_time < Luogu_time:
    print("Local")
elif Local_time > Luogu_time:
    print("Luogu")