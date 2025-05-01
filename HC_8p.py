class State:
    goal_state: 'State | None' = None

    def __init__(self, state, parent=None):
        self.state = tuple(state)
        self.parent = parent
        self.cost = self.calculate_cost()

    @staticmethod
    def distance(a, b):
        """Calculate Manhattan distance between two positions"""
        return abs(a // 3 - b // 3) + abs(a % 3 - b % 3)

    def calculate_cost(self):
        """Calculate total Manhattan distance for all tiles"""
        if not self.goal_state:
            return 0
        total = 0
        for i, val in enumerate(self.goal_state.state):
            if val != 0:  # Skip the blank tile
                try:
                    current_pos = self.state.index(val)
                    total += self.distance(current_pos, i)
                except ValueError:
                    # Handle case where tile is missing (shouldn't happen for valid puzzles)
                    pass
        return total

    def __repr__(self):
        """Pretty-print the puzzle state"""
        s = " ".join(map(str, self.state)).replace("0", ".")
        return f"{s[:5]}\n{s[6:11]}\n{s[12:]}"

    def swap(self, a, b):
        """Swap two tiles and return new State"""
        new_state = list(self.state)
        new_state[a], new_state[b] = new_state[b], new_state[a]
        return State(new_state, self)

    def generate_neighbors(self):
        """Generate all possible next states by moving the blank tile"""
        gap = self.state.index(0)
        neighbors = []
        
        # Generate moves in consistent order (up, down, left, right)
        if gap > 2:  # Can move up
            neighbors.append(self.swap(gap, gap - 3))
        if gap < 6:  # Can move down
            neighbors.append(self.swap(gap, gap + 3))
        if gap % 3 > 0:  # Can move left
            neighbors.append(self.swap(gap, gap - 1))
        if gap % 3 < 2:  # Can move right
            neighbors.append(self.swap(gap, gap + 1))
            
        return neighbors

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state


def hill_climbing(current_state, max_steps=1000):
    """Hill climbing algorithm with cycle detection and step limit"""
    path = [current_state]
    visited = set([current_state])
    
    for _ in range(max_steps):
        if current_state.cost == 0:
            break  # Goal reached
            
        neighbors = current_state.generate_neighbors()
        if not neighbors:
            break  # No moves available
            
        # Filter out already visited states
        neighbors = [n for n in neighbors if n not in visited]
        if not neighbors:
            break  # All moves lead to visited states
            
        # Find the best neighbor (lowest cost)
        best_neighbor = min(neighbors, key=lambda x: x.cost)
        
        if best_neighbor.cost >= current_state.cost:
            break  # Local minimum reached
            
        # Move to the best neighbor
        current_state = best_neighbor
        path.append(current_state)
        visited.add(current_state)
    
    return path


if __name__ == "__main__":
    # Set the goal state
    State.goal_state = State((1, 2, 3, 8, 0, 4, 7, 6, 5))
    
    # Define starting state
    start = State((2, 8, 3, 1, 6, 4, 7, 0, 5))
    
    # Run hill climbing
    solution_path = hill_climbing(start)
    
    # Print the solution path
    for step, state in enumerate(solution_path):
        print(f"Step {step} (Cost: {state.cost}):")
        print(state)
        print("-----")
    
    # Check if goal was reached
    if solution_path[-1].cost == 0:
        print(f"Solution found in {len(solution_path)-1} moves!")
    else:
        print("Stuck in local minimum.")
        print(f"Best achieved cost: {solution_path[-1].cost}")