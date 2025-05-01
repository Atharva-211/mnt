from itertools import permutations

def solve_cryptarithmetic(word1, word2, result):
    # Combine all unique characters
    unique_chars = set(word1 + word2 + result)
    
    if len(unique_chars) > 10:
        print("Too many unique characters (more than 10). Cannot assign unique digits.")
        return

    letters = ''.join(unique_chars)
    first_letters = set([word1[0], word2[0], result[0]])  # leading zero not allowed

    for perm in permutations(range(10), len(letters)):
        char_digit = dict(zip(letters, perm))
        if any(char_digit[fl] == 0 for fl in first_letters):
            continue

        w1 = int(''.join(str(char_digit[c]) for c in word1))
        w2 = int(''.join(str(char_digit[c]) for c in word2))
        res = int(''.join(str(char_digit[c]) for c in result))

        if w1 + w2 == res:
            print(f"{word1}: {w1}, {word2}: {w2}, {result}: {res}")
            return

    print("No solution found.")

# --- User Input Section ---
w1 = input("Enter first word: ").upper()
w2 = input("Enter second word: ").upper()
res = input("Enter result word: ").upper()

solve_cryptarithmetic(w1, w2, res)
