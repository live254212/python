"""from tkinter import *
master = Tk() 
w = Scale(master, from_=0, to=42) 
w.pack() 
w = Scale(master, from_=0, to=200, orient=HORIZONTAL) 
w.pack() 
mainloop() """

"""from tkinter import *
root = Tk() 
scrollbar = Scrollbar(root) 
scrollbar.pack( side = RIGHT, fill = Y ) 
mylist = Listbox(root, yscrollcommand = scrollbar.set ) 
for line in range(100): 
   mylist.insert(END, 'This is line number' + str(line)) 
mylist.pack( side = LEFT, fill = BOTH ) 
scrollbar.config(  ) 
mainloop() """

"""from tkinter import *
root = Tk() 
root.title('GfG') 
top = Toplevel() 
top.title('Python') 
top.mainloop() """

"""from tkinter import *
master = Tk() 
w = Spinbox(master, from_ = 0, to = 10) 
w.pack() 
mainloop() 
"""

"""from tkinter import *
m1 = PanedWindow() 
m1.pack(fill = BOTH, expand = 1) 
left = Entry(m1, bd = 5) 
m1.add(left) 
m2 = PanedWindow(m1, orient = VERTICAL) 
m1.add(m2) 
top = Scale( m2, orient = HORIZONTAL) 
m2.add(top) 
mainloop()"""

"""from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Pythonguides')
ws.geometry('400x300')
ws.config(bg='#04B2D9')

def validation():
    name = name_tf.get()
    msg = ''

    if len(name) == 0:
        msg = 'name can\'t be empty'
    else:
        try:
            if any(ch.isdigit() for ch in name):
                msg = 'Name can\'t have numbers'
            elif len(name) <= 2:
                msg = 'name is too short.'
            elif len(name) > 100:
                msg = 'name is too long.'
            else:
                msg = 'Success!'
        except Exception as ep:
            messagebox.showerror('error', ep)
        
    messagebox.showinfo('message', msg)
    
frame = Frame(
    ws,
    padx=10,
    pady=10
)
frame.pack(pady=20)

Label(
    frame,
    text='Enter Name'
).grid(row=0, column=1)

name_tf = Entry(
    frame,
    font = ('sans-sherif', 14)
)
name_tf.grid(row=0, column=1)

Button(
    frame,
    text='Submit',
    pady=10,
    padx=20,
    command=validation
).grid(row=1, columnspan=2)

ws.mainloop()"""




