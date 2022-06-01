#왕실의 나이트

loc = input()

x = int(loc[1])
y = int(ord(loc[0]) - int(ord("a")))  + 1

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

ans = 0

for i in range(0):
    nx = x + dx[i]
    ny = y +dy[i]

    if 9 > nx > 0 and 9 > ny > 0 :
        ans += 1

print(ans)
