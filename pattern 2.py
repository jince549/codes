limit = 5
for i in range(limit):
    for k in range(i):
        print(" ", end= "")
    for j in range(limit - i):
        print("*", end=" ")
    print()