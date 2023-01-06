import sys

for _ in range(3):
    N = int(input())
    n = [int(sys.stdin.readline()) for i in range(N)]
    if sum(n) == 0:
        print("0")
    if sum(n) > 0:
        print("+")
    if sum(n) < 0:
        print("-")
