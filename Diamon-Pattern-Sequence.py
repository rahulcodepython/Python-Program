row: int = 4

for i in range(row):
    start_value = 1
    s = 1

    for j in range((2 * row) - 1):
        if (j >= (row - i - 1)) and (j <= (row - 1 + i)):
            print(f" {start_value} ", end="")

            if j < row - 1:
                s += 1
                start_value += s
            else:
                start_value -= s
                s -= 1

        else:
            print("   ", end="")

    print()

for i in range(row):
    start_value = 1
    s = 1

    for j in range((2 * row) - 1):
        if (j >= i) and (j < ((2 * row) - 1) - i):
            print(f" {start_value} ", end="")

            if j < row - 1:
                s += 1
                start_value += s
            else:
                start_value -= s
                s -= 1
        else:
            print("   ", end="")
    print()
