#14916_그리디

n = int(input())
cnt=0

while n > 0:
    if n==1 or n==3:
        cnt-= 1
        n=0
        
    elif n % 5 == 0:
        n -= 5
        cnt += 1
    else:
        n -= 2
        cnt += 1


print(cnt)


