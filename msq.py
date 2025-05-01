def generate_magic_square(n):
    if n % 2 == 0:
        print("Only works for odd numbers!")
        return

    magic_square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2  # Start at middle of top row

    while num <= n * n:
        magic_square[i][j] = num
        num += 1

        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if magic_square[new_i][new_j]:  # Already filled
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic_square

def print_magic_square(square):
    n = len(square)
    for row in square:
        print(" ".join(f"{num:2d}" for num in row))
    print(f"Magic constant: {n * (n**2 + 1) // 2}")

# Example usage:
n = 3  # Must be odd
magic = generate_magic_square(n)
print_magic_square(magic)
