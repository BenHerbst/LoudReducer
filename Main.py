import tkinter as tk

window = tk.Tk()
window.title("LoudReducer - 1.0")
window.geometry('500x500')

reduceLoudSounds = tk.BooleanVar()

def print_selection():
    print(reduceLoudSounds.get())

reduceCheckBox = tk.Checkbutton(window, text='Reduce loud sounds',variable=reduceLoudSounds, onvalue=True, offvalue=False, command=print_selection)
reduceCheckBox.pack()

window.mainloop()