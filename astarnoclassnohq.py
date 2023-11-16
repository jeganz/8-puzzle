PUZZLE_SIZE = 3

def calculate_heuristic(state, goal_state):
    h = 0
    for i in range(PUZZLE_SIZE):
        for j in range(PUZZLE_SIZE):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h

def get_blank_position(state):
    for i in range(PUZZLE_SIZE):
        for j in range(PUZZLE_SIZE):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state, cost):
    neighbors = []
    i, j = get_blank_position(state)

    for action in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + action[0], j + action[1]
        if 0 <= new_i < PUZZLE_SIZE and 0 <= new_j < PUZZLE_SIZE:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append((new_state, cost + 1))

    return neighbors

def a_star(initial_state, goal_state):
    initial_node = (initial_state, None, 0, calculate_heuristic(initial_state, goal_state))
    queue = [initial_node]
    visited = set()

    while queue:
        queue.sort(key=lambda x: x[2] + x[3])  # Sort based on cost + heuristic
        current_node = queue.pop(0)

        if current_node[0] == goal_state:
            # Goal state reached
            path = []
            while current_node:
                path.append(current_node[0])
                current_node = current_node[1]
            return path[::-1]

        if tuple(map(tuple, current_node[0])) not in visited:
            visited.add(tuple(map(tuple, current_node[0])))
            neighbors = get_neighbors(current_node[0], current_node[2])
            for neighbor_state, neighbor_cost in neighbors:
                heuristic = calculate_heuristic(neighbor_state, goal_state)
                queue.append((neighbor_state, current_node, neighbor_cost, heuristic))

    return None

# Example usage:
# initial_state = [
#     [2, 6, 8],
#     [0, 1, 4],
#     [5, 3, 7]
# ]below test case failed
initial_state = [
    [0, 6, 1],
    [2, 3, 8],
    [5, 7, 4]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution_path = a_star(initial_state, goal_state)

if solution_path:
    l=[row[:]for row in solution_path]
    for state in solution_path:
        for row in state:
            print(row)
        print()
    print(l)
else:
    print("No solution found.")
