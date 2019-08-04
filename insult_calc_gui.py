from tkinter import *
from tkinter import ttk
from shakespeare_insult_calc import sqrt_or_insult

def calc_insult(*args):
    user_input = number.get()

    answer.set(sqrt_or_insult(user_input))

root = Tk()
root.title("Shakespeare Insult Calculator")

number = StringVar()
answer = StringVar()

frame = ttk.Frame(root, padding = (3, 3, 12, 12))

user_input = ttk.Entry(frame, textvariable = number)

frame.grid(column = 0, row = 0, sticky = (N, E, W, S))
user_input.grid(column = 0, row = 0, sticky = (N, E, W, S))
ttk.Button(frame, text = "Enter", command = calc_insult).grid(column = 0, row = 1, sticky = (N, E, W, S))
ttk.Label(frame, textvariable = answer).grid(column = 0, row = 2, sticky = (N, E, W, S))

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
frame.columnconfigure(0, weight = 1)
frame.rowconfigure(0, weight = 1)
frame.rowconfigure(1, weight = 1)
frame.rowconfigure(2, weight = 1)

for child in frame.winfo_children():
    child.grid_configure(padx = 3, pady = 3)

user_input.focus()
root.bind("<Return>", calc_insult)

root.mainloop()