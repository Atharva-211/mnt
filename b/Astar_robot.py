import heapq

DIRS = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}

class Node:
    def __init__(self, x, y, cost, path):
        self.x = x
        self.y = y
        self.cost = cost
        self.path = path
        self.heuristic = 0

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def a_star_robot(grid, start, goal):
    sx, sy = start
    gx, gy = goal

    visited = set()
    heap = []

    start_node = Node(sx, sy, 0, [])
    start_node.heuristic = manhattan_distance(sx, sy, gx, gy)
    heapq.heappush(heap, start_node)

    while heap:
        current = heapq.heappop(heap)

        if (current.x, current.y) == (gx, gy):
            return current.path

        if (current.x, current.y) in visited:
            continue
        visited.add((current.x, current.y))

        for move, (dx, dy) in DIRS.items():
            nx, ny = current.x + dx, current.y + dy
            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                new_node = Node(nx, ny, current.cost + 1, current.path + [move])
                new_node.heuristic = manhattan_distance(nx, ny, gx, gy)
                heapq.heappush(heap, new_node)

    return None  # No path found

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start = (0, 0)
    goal = (3, 3)
    
    path = a_star_robot(grid, start, goal)
    if path:
        print(len(path))
        for move in path:
            print(move)
    else:
        print("No path found")
