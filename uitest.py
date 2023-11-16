from time import sleep
import tkinter as tk
import customtkinter as ck

def on_box_click(box_number):
    label.config(text=f"Box {box_number} clicked!")

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
root.configure(background='#ECE3CE')

# Create and pack widgets
frame = ck.CTkFrame(master=root,fg_color='transparent',border_width=3,corner_radius=10,border_color='#4F6F52')
frame.place(relx=0.5,rely=0.5,anchor=ck.CENTER)
def button_function():
    global m
    for m1 in m:
        root.update()
        sleep(.8)
        c=0
        for i in range(3):
            for j in range(3):
                if m1[i][j]==0:
                    col='transparent'
                    btext=''
                else:
                    col='#739072'
                    btext=f'{m1[i][j]}'
                boxes[c].configure(text=btext,fg_color=col)
                c+=1
        

# Use CTkButton instead of tkinter Button
button = ck.CTkButton(master=root, text="Solve", command=button_function,font=('Century Gothic',20,'bold'),fg_color='#4F6F52')
button.place(relx=0.1, rely=0.1, anchor=ck.CENTER)

m=[[[0, 6, 1], [2, 3, 8], [5, 7, 4]], [[6, 0, 1], [2, 3, 8], [5, 7, 4]], [[6, 1, 0], [2, 3, 8], [5, 7, 4]], [[6, 1, 8], [2, 3, 0], [5, 7, 4]], 
   [[6, 1, 8], [2, 0, 3], [5, 7, 4]], [[6, 0, 8], [2, 1, 3], [5, 7, 4]], [[0, 6, 8], [2, 1, 3], [5, 7, 4]], [[2, 6, 8], [0, 1, 3], [5, 7, 4]], 
   [[2, 6, 8], [1, 0, 3], [5, 7, 4]], [[2, 6, 8], [1, 3, 0], [5, 7, 4]], [[2, 6, 0], [1, 3, 8], [5, 7, 4]], [[2, 0, 6], [1, 3, 8], [5, 7, 4]], 
   [[2, 3, 6], [1, 0, 8], [5, 7, 4]], [[2, 3, 6], [1, 7, 8], [5, 0, 4]], [[2, 3, 6], [1, 7, 8], [5, 4, 0]], [[2, 3, 6], [1, 7, 0], [5, 4, 8]], 
   [[2, 3, 0], [1, 7, 6], [5, 4, 8]], [[2, 0, 3], [1, 7, 6], [5, 4, 8]], [[0, 2, 3], [1, 7, 6], [5, 4, 8]], [[1, 2, 3], [0, 7, 6], [5, 4, 8]], 
   [[1, 2, 3], [5, 7, 6], [0, 4, 8]], [[1, 2, 3], [5, 7, 6], [4, 0, 8]], [[1, 2, 3], [5, 0, 6], [4, 7, 8]], [[1, 2, 3], [0, 5, 6], [4, 7, 8]], 
   [[1, 2, 3], [4, 5, 6], [0, 7, 8]], [[1, 2, 3], [4, 5, 6], [7, 0, 8]], [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
boxes=[]
for i in range(3):
    for j in range(3):
        if m[0][i][j]==0:
            col='transparent'
            btext=''
        else:
            col='#739072'
            btext=f'{m[0][i][j]}'
        box = ck.CTkButton(frame, text=btext, width=70, height=70,corner_radius=10, 
                        fg_color=col,font=('Century Gothic',20,'bold'),text_color='#3A4D39',hover='false')
        box.grid(row=i+1, column=j+1, padx=4, pady=4)
        boxes.append(box)  


# Run the Tkinter event loop
root.mainloop()
