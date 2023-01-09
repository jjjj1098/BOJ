x, y = map(int, input().split())

m = abs((x-1)%4 - (y-1)%4)

n = abs((x-1)//4 - (y-1)//4)

print(m+n)