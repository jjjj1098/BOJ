#큰수의법칙
n, m, k = map(int, input().split())
num = map(int, input().split())

num.sort(reverse=True)
ans = 0
count = 0 

for i in range(m):
    if count < k:
        ans += num[0]
        count += 1
    else:
        ans += num[1]
        count = 0
