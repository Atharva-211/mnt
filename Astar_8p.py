import heapq

class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost  # f(n) = g(n) + h(n)
        self.blank_pos = board.index(0)  # Cache blank position

    def __lt__(self, other):
        return self.cost < other.cost

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
    print()

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

moves = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1
}

def heuristic(board):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(board[i] - 1, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def is_solvable(board):
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] != 0 and board[j] != 0 and board[i] > board[j]:
                inversions += 1
    return inversions % 2 == 0

def a_star(start_state):
    if not is_solvable(start_state):
        return None

    open_list = []
    closed_list = set()
    heapq.heappush(open_list, PuzzleState(start_state, None, None, 0, heuristic(start_state)))

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.board == goal_state:
            return current_state

        closed_list.add(tuple(current_state.board))

        for move, delta in moves.items():
            if (move == 'Up' and current_state.blank_pos < 3) or \
               (move == 'Down' and current_state.blank_pos > 5) or \
               (move == 'Left' and current_state.blank_pos % 3 == 0) or \
               (move == 'Right' and current_state.blank_pos % 3 == 2):
                continue

            new_board = current_state.board[:]
            new_blank_pos = current_state.blank_pos + delta
            new_board[current_state.blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[current_state.blank_pos]

            if tuple(new_board) in closed_list:
                continue

            new_state = PuzzleState(
                new_board,
                current_state,
                move,
                current_state.depth + 1,
                current_state.depth + 1 + heuristic(new_board)
            )
            heapq.heappush(open_list, new_state)

    return None

def print_solution(solution):
    path = []
    current = solution
    while current:
        path.append(current)
        current = current.parent
    path.reverse()

    print("Solution Steps:")
    for i, step in enumerate(path):
        if step.move:
            print(f"Step {i}: Move {step.move}")
        else:
            print(f"Step {i}: Initial State")
        print_board(step.board)
    print(f"Total moves: {len(path)-1}")

initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
solution = a_star(initial_state)

if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution exists.")