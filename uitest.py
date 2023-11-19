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
m=[[0, 6, 1], [2, 3, 8], [5, 7, 4]]

def inputing():
    for i in inputs:
        if i.get()=='':
            return
    global m
    for i in range(3):
        for j in range(3):
            m[i][j]=int(inputs[3*i+j].get())
            inputs[3*i+j].destroy()
            if m[i][j]==0:
                col='transparent'
                btext=''
            else:
                col='#739072'
                btext=f'{m[i][j]}'
            boxes[3*i+j].configure(text=btext,fg_color=col)
    button.configure(text='Solve',command=button_function)

def validate(P):
    def validip(P):
        for i in inputs:
            if i.get() !='' and P==i.get():
                return False
        return True
    if len(P) == 1 and P.isdigit() and int(P)<9:
        return validip(P)
    elif len(P) == 0:
        # empty Entry is ok
        return True
    else:
        # Anything else, reject it
        return False
def button_function():
    # global m
    # for m1 in m:
    #     root.update()
    #     sleep(.8)
    #     c=0
    #     for i in range(3):
    #         for j in range(3):
    #             if m1[i][j]==0:
    #                 col='transparent'
    #                 btext=''
    #             else:
    #                 col='#739072'
    #                 btext=f'{m1[i][j]}'
    #             boxes[c].configure(text=btext,fg_color=col)
    #             c+=1
    button.configure(text='Done',command=inputing)
    for i in range(3):
        for j in range(3):
            vcmd = (root.register(validate), '%P')
            input=ck.CTkEntry(frame,width=70,height=70,font=('Century Gothic',20,'bold'),fg_color='#739072',corner_radius=10,
                                    bg_color='transparent',text_color='#3A4D39',border_width=0,justify='center',validate='key',validatecommand=vcmd)
            input.grid(row=i+1, column=j+1, padx=4, pady=4)
            inputs.append(input)
        

# Use CTkButton instead of tkinter Button
button = ck.CTkButton(master=root, text="Solve", command=button_function,font=('Century Gothic',20,'bold'),fg_color='#4F6F52')
button.place(relx=0.1, rely=0.1, anchor=ck.CENTER)

boxes=[]
inputs=[]

for i in range(3):
    for j in range(3):
        if m[i][j]==0:
            col='transparent'
            btext=''
        else:
            col='#739072'
            btext=f'{m[i][j]}'
        box = ck.CTkButton(frame, text=btext, width=70, height=70,corner_radius=10, 
                        fg_color=col,font=('Century Gothic',20,'bold'),text_color='#3A4D39',hover='false')
        box.grid(row=i+1, column=j+1, padx=4, pady=4)
        boxes.append(box)  


# Run the Tkinter event loop
root.mainloop()
