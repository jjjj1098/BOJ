A, B = map(int, input().split())
C = int(input())

hour = (B + C) // 60
min = (B + C) % 60

if B+C >= 60:
    if A+hour >= 24:
        A -= 24
    A += hour
    B = min
else:
    if A>=24:
        A -= 24
    B += C


print(A, B)
