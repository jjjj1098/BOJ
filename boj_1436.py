N = int(input())
cnt = 0
ans = 666
while True:
    if '666' in str(ans):
        cnt += 1
    if cnt == N:
        print(ans)
        break
    ans += 1