import heapq

# A* Search Node class
class Node:
    def __init__(self, city, cost, heuristic, path):
        self.city = city
        self.cost = cost
        self.heuristic = heuristic
        self.path = path

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def a_star(graph, start, end, heuristic):
    # Priority queue for the A* search
    open_list = []
    heapq.heappush(open_list, Node(start, 0, heuristic[start], []))
    
    # Visited cities set
    visited = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        current_city = current_node.city

        # If we reached the goal, return the path and cost
        if current_city == end:
            return current_node.cost, current_node.path + [current_city]

        # Mark the current city as visited
        if current_city in visited:
            continue
        visited.add(current_city)

        # Expand the neighbors
        for neighbor, weight in graph[current_city]:
            if neighbor not in visited:
                total_cost = current_node.cost + weight
                heapq.heappush(open_list, Node(neighbor, total_cost, heuristic.get(neighbor, 0), current_node.path + [current_city]))

    return float('inf'), []  # No path found

# Example usage
if __name__ == "__main__":
    cities = {
        'A': [('B', 5), ('C', 10)],
        'B': [('A', 5), ('C', 3), ('D', 2)],
        'C': [('A', 10), ('B', 3), ('D', 1), ('E', 7)],
        'D': [('B', 2), ('C', 1), ('E', 2)],
        'E': [('C', 7), ('D', 2)]
    }

    heuristic = {
        'A': 9,  # Approximate straight-line distance to E
        'B': 6,  # Approximate straight-line distance to E
        'C': 3,  # Approximate straight-line distance to E
        'D': 2,  # Approximate straight-line distance to E
        'E': 0   # Goal city, heuristic = 0
    }

    start = 'A'
    destination = 'E'
    
    distance, path = a_star(cities, start, destination, heuristic)

    print("Shortest distance:", distance)
    print("Path:", " -> ".join(path))
