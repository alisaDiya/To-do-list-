from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
        messagebox.showinfo("Success", "Task added successfully.")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def deleteTask():
    try:
        selected_task_index = lb.curselection()[0]
        lb.delete(selected_task_index)
        messagebox.showinfo("Success", "Task deleted successfully.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('TO DO LIST , TASK 2 ')
ws.config(bg='#ffc0cb')  # Set background color to pink
ws.resizable(width=False, height=False)

frame = Frame(ws, bg='#ffc0cb')  # Set background color to pink
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 12),  # Changed font size to 14
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    
    'Complete 1st task of technohacks'
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws, bg='#ffc0cb')  # Set background color to pink
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times', 14),  # Changed font size to 14
    bg='#add8e6',  # Changed to pink
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times', 14),  # Changed font size to 14
    bg='#add8e6',  # Changed to pink
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
