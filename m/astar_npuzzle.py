import heapq
import copy

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Find position of 0 (empty tile)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors by sliding tiles into the empty space
def get_neighbors(state):
    x, y = find_zero(state)
    moves = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

# A* Algorithm
def a_star(start):
    # Priority queue: (f, g, state, path)
    open_list = []
    closed_list = set()

    g = 0  # Cost to reach start
    h = heuristic(start)  # Heuristic cost
    f = g + h  # Total cost
    heapq.heappush(open_list, (f, g, start, []))  # Push start state into open list

    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)

        # If goal is reached
        if current_state == GOAL_STATE:
            print("Solution found!")
            for step in path + [current_state]:
                for row in step:
                    print(row)
                print()

            return path + [current_state]

        closed_list.add(tuple(map(tuple, current_state)))  # Add to closed list

        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) in closed_list:
                continue

            g_new = g + 1  # Path cost for neighbor
            h_new = heuristic(neighbor)  # Heuristic for neighbor
            f_new = g_new + h_new  # Total cost for neighbor

            # Push the neighbor into the open list
            heapq.heappush(open_list, (f_new, g_new, neighbor, path + [current_state]))

    print("No solution found.")
    return None

# Example Initial State (can be customized or randomized)
initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [6, 7, 8]]

print("Initial State:")
for row in initial_state:
    print(row)
print("\nRunning A*...\n")

solution = a_star(initial_state)