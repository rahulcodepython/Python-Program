length: int = 10
max_value: int = length * length

row_align: list[int] = [0, 1, 0, -1]
col_align: list[int] = [1, 0, -1, 0]

mat: list[list[int]] = [[0 for _ in range(length)] for _ in range(length)]


def isOdd(num: int) -> bool:
    return num % 2 != 0


def spiral_fill(value: int = 1, length: int = 4, index: int = 1, r: int = 0, c: int = -1) -> None:
    if isOdd(index):
        length = length
    else:
        length = length - 1

    row = row_align[(index - 1) % len(row_align)]
    col = col_align[(index - 1) % len(col_align)]

    for val in (range(value, (value + length))):
        r += row
        c += col
        value = val

        mat[r][c] = val

    if value == max_value:
        print(value, max_value)
        print("Value exceeds matrix size.")
        return

    print(value+1, length, index+1, r, c)

    spiral_fill(value+1, length, index+1, r, c)


spiral_fill(length=length)

for row in mat:
    print(row)
