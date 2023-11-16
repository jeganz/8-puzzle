from time import sleep
import tkinter as tk
import customtkinter as ck
from uiastar import Solver

# Create the main window
root = tk.Tk()
root.title("9 Boxes Grid")

# Set the window size
window_width = 1000
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
root.configure(background="#ECE3CE")

# Create and pack widgets
frame = ck.CTkFrame(
    master=root,
    fg_color="transparent",
    border_width=3,
    corner_radius=10,
    border_color="#4F6F52",
)
frame.place(relx=0.5, rely=0.5, anchor=ck.CENTER)


def Solve_function():
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    solution_path = Solver.a_star(m[0], goal_state)
    for m1 in solution_path:
        root.update()
        sleep(0.8)
        c = 0
        for i in range(3):
            for j in range(3):
                if m1[i][j] == 0:
                    col = "transparent"
                    btext = ""
                else:
                    col = "#739072"
                    btext = f"{m1[i][j]}"
                boxes[c].configure(text=btext, fg_color=col)
                c += 1
def shuffle_function():
    pass

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def movetile(x, y):
    x0, y0 = get_blank_position(m[0])
    for action in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if x == x0 + action[0] and y == y0 + action[1]:
            boxes[3 * x + y].configure(text="", fg_color="transparent")
            boxes[3 * x0 + y0].configure(text=str(m[0][x][y]), fg_color="#739072")
            root.update()
            m[0][x][y], m[0][x0][y0] = m[0][x0][y0], m[0][x][y]


# Use CTkButton instead of tkinter Button
shuffleButton = ck.CTkButton(
    master=root,
    text="Shuffle",
    command=shuffle_function,
    font=("Century Gothic", 20, "bold"),
    fg_color="#4F6F52",
)
shuffleButton.place(relx=0.5, rely=0.75, anchor=ck.CENTER)
solveButton = ck.CTkButton(
    master=root,
    text="Solve",
    command=Solve_function,
    font=("Century Gothic", 20, "bold"),
    fg_color="#4F6F52",
)
solveButton.place(relx=0.5, rely=0.85, anchor=ck.CENTER)

m = [[[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
boxes = []
for i in range(3):
    for j in range(3):
        if m[0][i][j] == 0:
            col = "transparent"
            btext = ""
        else:
            col = "#739072"
            btext = f"{m[0][i][j]}"
        box = ck.CTkButton(
            frame,
            text=btext,
            width=70,
            height=70,
            corner_radius=10,
            command=lambda x=i, y=j: movetile(x, y),
            fg_color=col,
            font=("Century Gothic", 20, "bold"),
            text_color="#3A4D39",
            hover="false",
        )
        box.grid(row=i + 1, column=j + 1, padx=4, pady=4)
        boxes.append(box)


# Run the Tkinter event loop
root.mainloop()