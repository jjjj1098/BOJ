ball = [1,2,3]
N = int(input())

for i in range(N):
    X, Y = map(int,input().split())
    x = ball.index(X)
    y = ball.index(Y)
    ball[x], ball[y] = ball[y], ball[x]

print(ball[0])