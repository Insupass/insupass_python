#gui-test
import tkinter
from tkinter import messagebox


def run_isopass():
    messagebox.showinfo('Isopass', 'hello')
    return()


def main():
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    b = tkinter.Button(root, text='run', command=run_isopass)
    b.pack()
    # root.geometry("400*300")
    # app = Example(root)
    root.mainloop()


main()
