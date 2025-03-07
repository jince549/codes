limit = 5
for i in range(limit):
    for k in range(limit - 1 - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()
bottom_limit = 3
for m in range (bottom_limit):
    for o in range(m + 1):
        print(" ", end="")
    for n in range(bottom_limit - m):
        print("*", end=" ")
    print()