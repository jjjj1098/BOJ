#숫자 카드 게임
import  sys
n, m = map(int, input().split())
arr = []
ans = []

for i in range (n):
    arr.append(list(map(int, sys.stdin.readline().split()))) 


for i in range(n):
    ans.append(arr[i][0])

print(arr[-1])