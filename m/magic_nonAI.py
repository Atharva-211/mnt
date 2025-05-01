def generate_magic_square(n):
    if n % 2 == 0:
        print("Only odd-order magic squares supported with this method.")
        return

    magic_square = [[0]*n for _ in range(n)]
    i, j = 0, n // 2

    for num in range(1, n*n + 1):
        magic_square[i][j] = num
        newi, newj = (i - 1) % n, (j + 1) % n
        if magic_square[newi][newj]:
            i += 1
        else:
            i, j = newi, newj

    for row in magic_square:
        print(" ".join(f"{num:2d}" for num in row))

# Take user input
try:
    n = int(input("Enter an odd number for the magic square size: "))
    generate_magic_square(n)
except ValueError:
    print("Please enter a valid integer.")
