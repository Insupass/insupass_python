# gui.py
# Yu Gui    01/12/2017
# GUI for IsoPass using tkinter
# NYU CIMS

from . import hash

import tkinter
from tkinter import messagebox


def run():
    # generate password by calling hash module
    # show password in a info message box
    def generate_pwd(*args):
        str_app_pwd = app_pwd.get()
        str_master_pwd = master_pwd.get()
        str_result = hash.run_hash(str_app_pwd, str_master_pwd)
        messagebox.showinfo('IsoPass', str_result)
        return ()

    # create root window instance
    root = tkinter.Tk()
    root.title('IsoPass')

    # declare entry vars
    app_pwd = tkinter.StringVar()
    master_pwd = tkinter.StringVar()

    # declare layout elements
    label_slogan = tkinter.Label(root, text='IsoPass')
    label_app_pwd = tkinter.Label(root, text='Application String')
    entry_app_pwd = tkinter.Entry(root, textvariable=app_pwd)
    label_master_pwd = tkinter.Label(root, text='Master Pwd')
    entry_master_pwd = tkinter.Entry(root, textvariable=master_pwd)
    button_generate = tkinter.Button(root, text='generate', command=generate_pwd)

    # place elements on the root window
    label_slogan.grid(row=0, padx=10, pady=20)
    label_app_pwd.grid(row=1, padx=10, pady=10)
    entry_app_pwd.grid(row=2, padx=10, pady=0)
    label_master_pwd.grid(row=3, padx=10, pady=10)
    entry_master_pwd.grid(row=4, padx=10, pady=0)
    button_generate.grid(row=5, padx=10, pady=10)

    # some adjustments
    root.bind('<Return>', generate_pwd)
    entry_app_pwd.focus()

    root.mainloop()
