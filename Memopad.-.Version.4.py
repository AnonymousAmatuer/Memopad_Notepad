from tkinter import *
from datetime import datetime
from tkinter import messagebox, Menu
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

editor = Tk()
editor.title('Memopad PAD')

# In the above line, where did you store the image icon? You have to write in here.
editor.resizable(0, 0)
# creating scrollable notepad window
pad = ScrolledText(editor, width=160, height=45)
File = ' '


def New_File():  # file menu New option
    global File
    if len(pad.get('1.0', END + '-1c')) > 0:  # -1c is used for the last character in the memopad
        if messagebox.askyesno("Memopad", "Do you want to save changes to text?"):
            Save_FIle()
        else:
            pad.delete(0.0, END)
    editor.title("Memopad")


def Open_file():  # file menu Open option
    fd = filedialog.askopenfile(parent=editor, mode='r')
    t = fd.read()  # t is the text read through filedialog
    pad.delete(0.0, END)
    pad.insert(0.0, t)


def Save_FIle():  # file menu Save option
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file != None:
        data = pad.get('1.0', END)
    try:
        file.write(data)
    except:
        messagebox.showerror(title="Error", message="Not able to save file!")
        if messagebox.askretrycancel("Retry", "Retry process?"):
            file.write(data)


def Save_File_as():  # file menu Save As option
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = pad.get(0.0, END)  # t stands for the text gotten from notepad
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message="Not able to save file!")
        if messagebox.askretrycancel("Retry", "Retry process?"):
            fd.write(t.rstrip())


def Exit_pad():  # file menu Exit option
    if messagebox.askyesno("memopad", "Are you sure you want to exit"):
        if messagebox.askyesno("memopad", "Are you sure you want to exit? (Confirmation)"):
            editor.destroy()


def Cut_Text():  # edit menu Cut option
    pad.event_generate("<<Cut>>")


def Copy_Text():  # edit menu Copy option
    pad.event_generate("<<Copy>>")


def Paste_Text():  # edit menu Paste option
    pad.event_generate("<<Paste>>")


def Select_All():  # edit menu Select All option
    pad.event_generate("<<SelectAll>>")


def Time_Date():  # edit menu Date/Time option
    now = datetime.now()
    # YYYY/mm/dd H:M:S
    dtString = now.strftime("%Y/%m/%d %H:%M:%S")
    messagebox.showinfo("Date/time", dtString)


def About_Notepad():  # help menu About option
    messagebox.showinfo("About Memopad", "Memopad by - \nAnonymousAmatuer™")
    messagebox.showinfo("About Memopad", " Thank you for using this software")



def Rate_Pad():  # lets user to rate the pad
    messagebox.showinfo("Memopad rating", "To rate you experience visit \n http://bitly.ws/hkXG")
    messagebox.showwarning("Memopad rating","I never store your information until you login with your email account. Sign out before submitting")


def features():  # Describes Features
    messagebox.showinfo("Memopad features",
                                "*Lets you to view files and code without converting to txt format \n *Note: Visuals not supported \n*Cut, Copy, Paste functions \n *Date and time feature ")
    messagebox.showinfo("New Memopad features", "New Fonts added. More Fonts will be added later.")



def updates():  # Describes the Updates in it
    messagebox.showinfo("Memopad Updates",
                        "*Update tab introduced \n* Updates introduced is shown here. \n *Added Fonts tab and removed updates tab \n No more disturbing welcoming messages")


def font_Ink():
    pad.config(font=('Ink Free', 12))
    pad.pack()


def clear():
    pad.delete(1.0, END)


def Helvet():
    pad.config(font=('Helvetica', 12))


def Times():
    pad.config(font=('Times', 12))


def version():
    messagebox.showinfo("Version", "You are currently using Version number 4.0 of MapPad")


padmenu: Menu = Menu(editor)
editor.configure(menu=padmenu)

# file menu
fileMenu = Menu(padmenu, tearoff=False)
padmenu.add_cascade(label='File', menu=fileMenu)

# adding options in file menu
fileMenu.add_command(label='New pad ', command=New_File)
fileMenu.add_command(label='Open pad', command=Open_file)
fileMenu.add_command(label='Save pad', command=Save_FIle)
fileMenu.add_command(label='Save pad As', command=Save_File_as)
fileMenu.add_separator()
fileMenu.add_command(label='Exit memopad', command=Exit_pad)

# edit menu
editMenu = Menu(padmenu, tearoff=False)
padmenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut text', command=Cut_Text)
editMenu.add_command(label='Copy text', command=Copy_Text)
editMenu.add_command(label='Paste text', command=Paste_Text)
editMenu.add_command(label='Clear', command=clear)
editMenu.add_separator()
editMenu.add_command(label='Select All text', command=Select_All)
editMenu.add_command(label='Date/Time', command=Time_Date)
editMenu.add_separator()

# help menu
helpMenu = Menu(padmenu, tearoff=False)
padmenu.add_cascade(label='Help', menu=helpMenu)

# adding options in help menu
helpMenu.add_command(label='About Memopad', command=About_Notepad)
helpMenu.add_command(label="Rate This Pad...", command=Rate_Pad)
helpMenu.add_command(label="Features", command=features)
helpMenu.add_command(label="Version Memopad", command=version)

# Update Menu
updatemenu = Menu(padmenu, tearoff=False)
padmenu.add_cascade(label='Updates', menu=updatemenu)
updatemenu.add_command(label='New Update', command=updates)

# Font Menu
fontmenu = Menu(padmenu, tearoff=False)
padmenu.add_cascade(label='Fonts', menu=fontmenu)
fontmenu.add_command(label='Ink Free', command=font_Ink)
fontmenu.add_command(label='Helvetica', command=Helvet)
fontmenu.add_command(label='TIMES', command=Times)

pad.pack()
editor.mainloop()