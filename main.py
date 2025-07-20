length: int = 4

row_align: list[int] = [0, 1, 0, -1]
col_align: list[int] = [1, 0, -1, 0]

mat: list[list[int]] = [[0 for _ in range(length)] for _ in range(length)]


def isOdd(num: int) -> bool:
    return num % 2 != 0


def spiral_fill(value: int = 1, length: int = 4, index: int = 1, r: int = 0, c: int = 0) -> None:
    if isOdd(index):
        length = length
    else:
        length = length - 1

    row = row_align[(index - 1) % len(row_align)]
    col = col_align[(index - 1) % len(col_align)]

    for i, val in enumerate(range(value, (value + length))):
        value = val
        print(f"[{r}, {c}] = {val}")

    #     if r < length:
    #         r += row
    #     if c < length:
    #         c += col

    #     # mat[r][c] = val

    # if value == length * length:
    #     return

    # spiral_fill(value+1, length, index+1, r, c)

    print(value+1, length, index+1, r, c)


spiral_fill()

for row in mat:
    print(row)
