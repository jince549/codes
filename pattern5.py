row = 7
column = 5
pattern = [[1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],
           [1, 1, 1, 1, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1]]

for i in range(row):
    for j in range(column):
        if pattern[i][j]:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()