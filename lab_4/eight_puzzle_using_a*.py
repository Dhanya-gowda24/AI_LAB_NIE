import heapq
from copy import deepcopy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

class Puzzle:
    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth  # g(n)
        self.zero_pos = self.find_zero()
        self.cost = self.depth + self.heuristic()  # f(n) = g(n) + h(n)

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def display(self):
        for row in self.board:
            print(row)
        print()

    def is_goal(self):
        return self.board == GOAL_STATE

    def heuristic(self):
        """Manhattan Distance"""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    goal_x = (value - 1) // 3
                    goal_y = (value - 1) % 3
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def generate_successors(self):
        successors = []
        x, y = self.zero_pos

        moves = {
            "Up": (x - 1, y),
            "Down": (x + 1, y),
            "Left": (x, y - 1),
            "Right": (x, y + 1)
        }

        for move_name, (new_x, new_y) in moves.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = deepcopy(self.board)
                
                # Swap 0 with adjacent tile
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                
                successors.append(Puzzle(
                    new_board,
                    parent=self,
                    move=f"Move {new_board[x][y]} {move_name}",
                    depth=self.depth + 1
                ))

        return successors

    def __lt__(self, other):
        return self.cost < other.cost


def a_star(initial_board):
    start = Puzzle(initial_board)
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            return current

        closed_set.add(str(current.board))

        for neighbor in current.generate_successors():
            if str(neighbor.board) not in closed_set:
                heapq.heappush(open_list, neighbor)

    return None


def print_solution(solution):
    path = []
    current = solution

    while current:
        path.append(current)
        current = current.parent

    path.reverse()

    print("Solution Steps:\n")
    for i, step in enumerate(path):
        if i > 0:
            print(f"Move {i}: {step.move}")
        step.display()


# Example Initial State
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Run A*
solution = a_star(initial_state)

# Print result
if solution:
    print_solution(solution)
else:
    print("No solution found.")



'''
output:
Solution Steps:

[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Move 1: Move 5 Down
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Move 2: Move 8 Right
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

'''
