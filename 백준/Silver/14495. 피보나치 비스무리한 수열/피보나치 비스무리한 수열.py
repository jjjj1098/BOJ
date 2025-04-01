n = int(input())


fib = [0, 1, 1, 1]
 
for i in range (4, 1+n):
    fib.append((fib[i-1] + fib[i-3]))

print(fib[n])


    