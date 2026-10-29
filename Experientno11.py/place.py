import tkinter as tk 
root = tk.Tk() 
root.title("Place Example")
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")
button1.place(x=50, y=50)
button2.place(x=100, y=100)
button3.place(x=150, y=150)

root.mainloop()