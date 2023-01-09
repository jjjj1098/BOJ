ball = [1,2,3]
N = input()
ans = 0
for i in range(N):
    X, Y = map(int,input().split())
    ball[X], ball[Y] = ball[Y], ball[X]

ball[0]