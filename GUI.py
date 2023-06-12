from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from subprocess import call
def Comp():
    call(["python", "Compare.py"])
def FIG():
    call(["python", "figure.py"])

headlabelfont = ("@Yu Gothic UI Semibold", 14, 'bold')
labelfont = ('Cambria', 14)
entryfont = ('Cambria', 12)


#my_dir = ''



"""def choseWav():
    wavFile = filedialog.askopenfilename(title='select a file',
                                                filetypes=(("wav file", "*.wav"),
                                                        ("all files", "*.*")))
    
    l1.config(text=wavFile)"""
def open_folder1():
    folder_path = filedialog.askdirectory()
    folder_label1.config(text="F1: " + folder_path)

def open_folder2():
    folder_path = filedialog.askdirectory()
    folder_label2.config(text="F2: " + folder_path)
    
main = tk.Tk()
main.title('Speaker Recognition ')
main.geometry('300x300+300+200')
main.resizable(0, 0)

Label(main, text="Speaker Recognition", font=headlabelfont, bg='White',relief=tk.GROOVE).pack(side=TOP, fill=X)

#frame
top_frame = Frame(main, bg="white")
top_frame.place(x=0, y=30, height=170, width=300)

bot_frame = Frame(main, bg="white")
bot_frame.place(x=0, y=200, height=100, width=300)

mid_frame = Frame(main, bg="black")
mid_frame.place(x=0, y=200, height=5, width=300)

#button 
Button(top_frame, text='Choose Folder', font=labelfont, width=11,command=open_folder1).place(x=130, y=10)
Button(top_frame, text='Choose Folder', font=labelfont, width=11,command=open_folder2).place(x=130, y=90)

# #Button(bot_frame, text='show the figure ', font=labelfont, width=15).place(x=800, y=350)
Button(bot_frame, text='Compare', font=entryfont, width=8,command=Comp).place(x=50, y=30)
Button(bot_frame, text='Figure', font=entryfont, width=8,command=FIG).place(x=150, y=30)

#l1=tk.Label(top_frame, text=my_dir,bg= 'white', font=11).place(x=0, y=0)

#Label
Label(top_frame, text='Folder 1: ',font=labelfont, width=9,bg="white").place(x=10,y=13)
Label(top_frame, text='Folder 2: ',font=labelfont, width=9,bg="white").place(x=10,y=93)
folder_label1 = tk.Label(top_frame, font=('labelfont', 10), width=40, bg="white")
folder_label1.place(x=10, y=54)

folder_label2 = tk.Label(top_frame, font=('labelfont', 10), width=40, bg="white")
folder_label2.place(x=10, y=134)

main.update()
main.mainloop()