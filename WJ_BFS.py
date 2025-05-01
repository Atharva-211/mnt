from collections import deque

# Jug capacities
MAX_A = 5
MAX_B = 3
goal = 2

def is_goal(state):
    a, b = state
    return a == goal or b == goal

def bfs():
    visited = set()
    queue = deque()
    
    # Each item: (a, b), path
    queue.append(((0, 0), []))
    
    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]
        print(f"Visiting: Jug A: {a}L, Jug B: {b}L")

        if is_goal((a, b)):
            print("\nReached goal!")
            for step in path:
                print(f"-> A: {step[0]}L, B: {step[1]}L")
            return True

        # Possible next states
        next_states = [
            (MAX_A, b),         # Fill A
            (a, MAX_B),         # Fill B
            (0, b),             # Empty A
            (a, 0),             # Empty B
            (a - min(a, MAX_B - b), b + min(a, MAX_B - b)),  # Pour A → B
            (a + min(b, MAX_A - a), b - min(b, MAX_A - a))   # Pour B → A
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    print("No solution found.")
    return False

# Run BFS
bfs()
