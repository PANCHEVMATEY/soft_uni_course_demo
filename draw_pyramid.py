rows = int(input())
for i in range(1, rows + 1):
    # Print spaces for alignment
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()