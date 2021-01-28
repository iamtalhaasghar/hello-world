import tkinter as tk
top = tk.Tk()

frame = tk.Frame(top)
frame.pack()

name = tk.Label(top, text = 'This is label.')
name.pack()

msg = tk.Message(top,text = "Playing with Tkinter...", bg= 'green')
msg.config(font=('consolas',24))
msg.pack()

b = tk.Button(frame,text='Exit',command= quit)
b.pack(side = tk.LEFT)


checkVar1 = tk.BooleanVar()

cb = tk.Checkbutton(top, text='Human',variable=checkVar1, onvalue=True, offvalue=False, height=3, width =20)
cb.pack()

top.mainloop()

