import tkinter as tk

count = 0

def update_label():
    label.config(text=str(count))

def increment():
    global count
    count += 1
    update_label()

def decrement():
    global count
    count -= 1
    update_label()

def reset(): 
    global count  
    count = 0
    update_label() 

root = tk.Tk()
root.title("Simple Counter")
root.configure(bg='lightblue')

label = tk.Label(root, text=str(count), font=("Arial", 40), fg='maroon', bg='lightblue')
label.pack(pady=20)

btn_increment = tk.Button(root, text="Increment", command=increment, bg='lightgreen', fg='green')
btn_increment.pack(side="left", padx=20, pady=20)

btn_decrement = tk.Button(root, text="Decrement", command=decrement, bg='pink', fg='red')
btn_decrement.pack(side="right", padx=20, pady=20)

btn_reset = tk.Button(root, text="Reset", command=reset, bg='grey')
btn_reset.pack(pady=55)

root.mainloop()
