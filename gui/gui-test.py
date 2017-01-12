#gui-test
import tkinter
from tkinter import messagebox



def generate_pwd():
    messagebox.showinfo('Isopass', str('hello' + app_pwd.get()))
    return()


def main():
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
    root.mainloop()


main()
