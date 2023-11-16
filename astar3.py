import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def calculate_heuristic(self):
        h = 0
        
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != goal_state[i][j] :
                    h += 1
        return h

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(node):
    neighbors = []
    i, j = get_blank_position(node.state)

    for action in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + action[0], j + action[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, node, node.cost + 1))

    return neighbors

def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)
    heap = [initial_node]
    visited = set()

    while heap:
        current_node = heapq.heappop(heap)

        if current_node.state == goal_state:
            # Goal state reached
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        if tuple(map(tuple, current_node.state)) not in visited:
            visited.add(tuple(map(tuple, current_node.state)))
            neighbors = get_neighbors(current_node)
            for neighbor in neighbors:
                heapq.heappush(heap, neighbor)

    return None

# Example usage:
initial_state =[[2, 6, 8],
                [0, 1, 4],
                [5, 3, 7]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
solution_path = a_star(initial_state)

if solution_path:
    l=[]
    for state in solution_path:
        l.append(state)
        for row in state:
            print(row)
        print()
    print(l)
else:
    print("No solution found.")
