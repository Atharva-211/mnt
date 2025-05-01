def water_jug_dfs(max_a, max_b, target):
    visited = set()  # To keep track of visited states
    path = []        # To record the solution path

    def dfs(a, b):
        # Base case: target reached
        if a == target or b == target:
            path.append((a, b))
            return True
        
        # Skip if state already visited
        if (a, b) in visited:
            return False
        
        visited.add((a, b))
        path.append((a, b))

        # Try all possible operations:
        # 1. Fill Jug A
        if a < max_a and dfs(max_a, b):
            return True
        # 2. Fill Jug B
        if b < max_b and dfs(a, max_b):
            return True
        # 3. Empty Jug A
        if a > 0 and dfs(0, b):
            return True
        # 4. Empty Jug B
        if b > 0 and dfs(a, 0):
            return True
        # 5. Pour from A to B
        if a > 0 and b < max_b:
            pour = min(a, max_b - b)
            if dfs(a - pour, b + pour):
                return True
        # 6. Pour from B to A
        if b > 0 and a < max_a:
            pour = min(b, max_a - a)
            if dfs(a + pour, b - pour):
                return True
        
        # Backtrack if no solution found from this state
        path.pop()
        return False

    # Start DFS from (0, 0)
    if dfs(0, 0):
        print("Solution Path:")
        for state in path:
            print(f"Jug A: {state[0]}L, Jug B: {state[1]}L")
    else:
        print("No solution exists.")

# Example usage:
water_jug_dfs(max_a=5, max_b=4, target=2)