import tkinter as tk
import math

root=tk.Tk()
root.title("nihao")
root.geometry("500x500")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=100, insertwidth=2, width=26, borderwidth=10)
display.grid(row=0, column=0, columnspan=4)

root.mainloop()