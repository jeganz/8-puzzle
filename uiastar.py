import heapq

class Solver:

    PUZZLE_SIZE = 3

    @staticmethod
    def calculate_heuristic(state, goal_state):
        h = 0
        for i in range(Solver.PUZZLE_SIZE):
            for j in range(Solver.PUZZLE_SIZE):
                if state[i][j] != goal_state[i][j]:
                    h += 1
        return h

    @staticmethod
    def get_blank_position(state):
        for i in range(Solver.PUZZLE_SIZE):
            for j in range(Solver.PUZZLE_SIZE):
                if state[i][j] == 0:
                    return i, j

    @staticmethod
    def get_neighbors(state, cost):
        neighbors = []
        i, j = Solver.get_blank_position(state)

        for action in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + action[0], j + action[1]
            if 0 <= new_i < Solver.PUZZLE_SIZE and 0 <= new_j < Solver.PUZZLE_SIZE:
                new_state = [row[:] for row in state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                neighbors.append((new_state, cost + 1))

        return neighbors

    @staticmethod
    def a_star(initial_state, goal_state):
        initial_node = (initial_state, None, 0, Solver.calculate_heuristic(initial_state, goal_state))
        heap = [(initial_node[2] + initial_node[3], initial_node)]
        visited = set()

        while heap:
            _, current_node = heapq.heappop(heap)

            if current_node[0] == goal_state:
                # Goal state reached
                path = []
                while current_node:
                    path.append(current_node[0])
                    current_node = current_node[1]
                return path[::-1]

            if tuple(map(tuple, current_node[0])) not in visited:
                visited.add(tuple(map(tuple, current_node[0])))
                neighbors = Solver.get_neighbors(current_node[0], current_node[2])
                for neighbor_state, neighbor_cost in neighbors:
                    heuristic = Solver.calculate_heuristic(neighbor_state, goal_state)
                    heapq.heappush(heap, (neighbor_cost + heuristic, (neighbor_state, current_node, neighbor_cost, heuristic)))

        return None

