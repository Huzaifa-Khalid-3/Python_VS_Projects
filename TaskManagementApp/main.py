from tkinter import *

task_management_application  = Tk()

def setup_window():
    task_management_application.geometry("800x500")
    setup_labels(task_management_application)
    setup_entries()
    setup_buttons()
    task_management_application.mainloop()

def setup_labels(task_management_application):
    main_heading_label = Label(task_management_application,text="Task Management Application",font=('Arial',30,'bold'))
    sub_heading_label = Label(task_management_application, text="Organize your tasks and stay productive")   
    new_task_label = Label(task_management_application,text="Enter a New Task")
    new_task_label.place(x=30,y=90)
    main_heading_label.pack()
    sub_heading_label.pack()

def setup_entries():
    new_task_entry = Entry(task_management_application,width=40)
    new_task_entry.place(x=30,y=110)

def setup_buttons():
    new_task_button = Button(task_management_application,text="Add task")
    new_task_button.place(x=290,y=106)
    
setup_window()