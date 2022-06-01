#2864

a, b = input().split()

min1 = int(a.replace('6', '5')) +int(b.replace('6', '5'))
max1 = int(a.replace('5', '6')) +int(b.replace('5', '6'))

print(min1, max1)