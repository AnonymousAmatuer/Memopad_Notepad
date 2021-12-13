from tkinter import *
from tkinter import messagebox

from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import asksaveasfilename


root = Tk()
root.title('Map-pad PAD')
file_path = ''
root.resizable(0, 0)

notepad = ScrolledText(root, width=90, height=40)
fileName = ' '


def set_file_path(path):
    global file_path
    file_path = path



def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Text Files', '*.txt')])  # To save a file extension
    else:
        path = file_path
    with open(path, 'w') as file:
        text = editor.get('1.0', END)
        file.write(text)
        set_file_path(path)


menu_bar=Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Save pad file', command=save_as)
file_menu.add_command(label='Save pad file as', command=save_as)
file_menu.add_command(label='Exit Map-pad', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)



root.config(menu=menu_bar)

editor = Text()


screen = Text(height=45)
screen.pack()
messagebox.showinfo("Simplified Memopad!","Hey There!\nThis is my simplified memopad notepad which is the first pad I made!! ")

root.mainloop()
