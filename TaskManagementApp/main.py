from tkinter import *


def setup_window():
    task_management_application = Tk()
    task_management_application.geometry("800x500")
    main_heading = Label(task_management_application,text="Task Management Application",font=('Arial',30,'bold'))
    sub_heading = Label(task_management_application, text="Organize your tasks and stay productive")   
    main_heading.pack()
    sub_heading.pack()
    task_management_application.mainloop()

setup_window()