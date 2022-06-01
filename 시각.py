#시각

n = int(input())
ans = 0

for i in range(n+1):
    for k in range(60):
        for j in range(60):
            if '3' in str(i)+str(k)+str(j):
                 ans += 1

print(ans)