limit = 6
for i in range(1, limit):
    for k in range (limit - i - 1):
        print(" ", end=" ")

    for j in range((i * 2) - 1):
        print("*", end=" ")
    print()
    