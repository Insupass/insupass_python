#gui-test
import tkinter
from tkinter import messagebox

import ip_hashing


def gui_main():
    def generate_pwd(*args):
        str_app_pwd = app_pwd.get()
        str_master_pwd = master_pwd.get()
        str_result = ip_hashing.run_hash(str_app_pwd, str_master_pwd)
        messagebox.showinfo('Isopass', str_result)
        return ()

    root = tkinter.Tk()
    root.title('IsoPass')
    root.geometry('300x400')

    app_pwd = tkinter.StringVar()
    master_pwd = tkinter.StringVar()
    app_pwd_label = tkinter.Label(root, text='Application String')
    app_pwd_entry = tkinter.Entry(root, textvariable=app_pwd)
    master_pwd_label = tkinter.Label(root, text='Master Pwd')
    master_pwd_entry = tkinter.Entry(root, textvariable=master_pwd)
    generate_button = tkinter.Button(root, text='generate', command=generate_pwd)

    app_pwd_label.pack()
    app_pwd_entry.pack()
    master_pwd_label.pack()
    master_pwd_entry.pack()
    generate_button.pack()

    root.bind('<Return>', generate_pwd)
    app_pwd_entry.focus()
    root.mainloop()

#init GUI
gui_main()