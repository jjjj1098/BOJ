while True:
    N = input()
    if N == "0":
        break
    print((len(N)+1) + sum([2 if element=="1" else 4 if element=="0" else 3 for element in N]))