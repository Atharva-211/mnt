from itertools import permutations

def solve_cryptarithmetic(puzzle):
    """
    Solves cryptarithmetic puzzles like SEND + MORE = MONEY
    Returns solution in format {'SEND': 9567, 'MORE': 1085, 'MONEY': 10652}
    """
    # Extract all unique letters
    letters = sorted(set(char for word in puzzle for char in word if char.isalpha()))
    if len(letters) > 10:
        return None  # Cannot solve with base-10 digits
    
    # Split puzzle into left and right of '='
    left, right = puzzle.split('=')
    left_terms = [term.strip() for term in left.split('+')]
    right_term = right.strip()
    all_terms = left_terms + [right_term]
    
    # First letters cannot be zero
    first_letters = {term[0] for term in all_terms}
    
    # Try all possible digit assignments
    for digits in permutations(range(10), len(letters)):
        # Skip if any first letter is assigned 0
        if any(digits[letters.index(letter)] == 0 for letter in first_letters):
            continue
        
        # Create digit mapping
        mapping = {letters[i]: digit for i, digit in enumerate(digits)}
        
        # Evaluate all terms
        term_values = {}
        valid = True
        
        for term in all_terms:
            num = 0
            for char in term:
                num = num * 10 + mapping[char]
            term_values[term] = num
        
        # Check if equation holds
        left_sum = sum(term_values[term] for term in left_terms)
        if left_sum == term_values[right_term]:
            return term_values
    
    return None  # No solution found

# Example usage
if __name__ == "__main__":
    puzzle = "NOON + MOON + SOON = JUNE"
    solution = solve_cryptarithmetic(puzzle)
    
    if solution:
        print("Solution found:")
        # Get all terms in the original order
        left, right = puzzle.split('=')
        terms = [term.strip() for term in left.split('+')] + [right.strip()]
        
        # Format the output as requested
        output = ", ".join(f"{term}: {solution[term]}" for term in terms)
        print(output)
    else:
        print("No solution exists")