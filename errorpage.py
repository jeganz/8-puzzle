from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import ctypes as ct

class errpopup:
    def __init__(self,msg) -> None:
        r=Toplevel()
        warn=ImageTk.PhotoImage(Image.open('warning icon.png').resize((80,80)))
        r.overrideredirect(True)
        def moveapp(e):
            global height
            r.geometry('300x'+str(height)+f'+{e.x_root}+{e.y_root}')
        r.bind('<B1-Motion>',moveapp)
        global height,status,fheight
        height=250
        fheight=0
        status='forward'

        def resize():
            r.destroy()
        r.geometry('300x'+str(height)+'+600+350')
        redf=customtkinter.CTkFrame(r,height=100,fg_color='#f65656',corner_radius=0)
        redf.pack(fill=X)
        warnicon=customtkinter.CTkLabel(redf,text='',image=warn).place(relx=.5,rely=.5,anchor=CENTER)

        errheading=customtkinter.CTkLabel(r,text="ERROR!",text_color='black',font=('Century Gothic', 25,'bold'))
        errheading.pack(pady=25)

        errmsg=customtkinter.CTkLabel(r,
                                    text=msg,
                                    text_color='red',fg_color='transparent',font=('Century Gothic', 12),anchor='w',wraplength=200)
        errmsg.place(relx=0.5,rely=0.7,anchor=CENTER)

        customtkinter.CTkButton(r,text='CLOSE',command=resize,width=100,corner_radius=30,fg_color='#f65656',
                                font=('Century Gothic', 12,'bold')).place(relx=.5,rely=.88,anchor=CENTER)

        r.mainloop()