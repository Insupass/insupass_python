#gui-test
import tkinter
from tkinter import messagebox


def main():
    def generate_pwd(*args):
        app_pwd_str = app_pwd.get()
        master_pwd_str = master_pwd.get()
        messagebox.showinfo('Isopass', str('hello'+app_pwd_str+master_pwd_str))
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


main()
