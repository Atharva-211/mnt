import heapq

MAX_CITIES = 100
INF = float('inf')

# Graph as adjacency list
graph = [[] for _ in range(MAX_CITIES)]
num_cities = 6  # Set this according to your graph size

# Add edge to the undirected graph
def add_edge(city1, city2, cost):
    graph[city1].append((city2, cost))
    graph[city2].append((city1, cost))

# Best First Search using a priority queue
def best_first_search(start, goal):
    visited = [False] * MAX_CITIES
    parent = [-1] * MAX_CITIES
    total_cost = 0

    min_heap = []
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        cost, city = heapq.heappop(min_heap)

        if visited[city]:
            continue
        visited[city] = True
        total_cost += cost

        print(f"Visiting City {city} (Cost: {cost})")

        if city == goal:
            print(f"Reached destination City {goal}! Total cost: {total_cost}")
            # Backtrack to find path
            path = []
            while city != -1:
                path.append(city)
                city = parent[city]
            path.reverse()
            print("Path:", " -> ".join(map(str, path)))
            return

        for neighbor, edge_cost in graph[city]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_cost, neighbor))
                parent[neighbor] = city

    print(f"No path found from City {start} to City {goal}.")

# Main setup
if __name__ == "__main__":
    # Initialize graph edges
    add_edge(0, 1, 4)
    add_edge(0, 2, 2)
    add_edge(1, 2, 5)
    add_edge(1, 3, 10)
    add_edge(2, 3, 3)
    add_edge(3, 4, 8)
    add_edge(4, 5, 6)

    start_city = 0
    goal_city = 5
    print(f"Shortest Path from City {start_city} to City {goal_city}")
    best_first_search(start_city, goal_city)