# Initial state
initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8]
]

# Solution steps
solution_steps = [
    "Down", "Left", "Up", "Up", "Right", "Down", "Down", "Left", "Up", "Up", "Right", 
    "Down", "Left", "Left", "Up", "Right", "Down", "Right", "Up", "Left", "Left", 
    "Down", "Right", "Down"
]

# List of matrices as a solution
solution_matrices = [initial_state]

# Apply each step to generate the solution matrices
current_matrix = initial_state
for step in solution_steps:
    if step == "Up":
        current_matrix = move_up(current_matrix)
    elif step == "Down":
        current_matrix = move_down(current_matrix)
    elif step == "Left":
        current_matrix = move_left(current_matrix)
    elif step == "Right":
        current_matrix = move_right(current_matrix)
    
    solution_matrices.append(current_matrix)

# Print the list of matrices as a solution
for idx, matrix in enumerate(solution_matrices, start=1):
    print(f"Step {idx}:")
    print_matrix(matrix)
    print()
