import tkinter as tk
import random
# GUI
# graphical user interface

root = tk.Tk()

loop_random = True

def start_random():
    global loop_random
    loop_random = True
    button["command"] = stop_random
    button["text"] = "Stop"
    print("Picking random.")
    pick_random()


def pick_random():
    if loop_random:
        number = random.randint(1, 6)
        # Add some text to the label
        label["text"] = number
        root.after(25, pick_random)


def stop_random():
    global loop_random
    loop_random = False
    button["command"] = start_random
    button["text"] = "Roll die"
    print("Stopping random.")


# Create the "widget"
label = tk.Label()
# Add to the screen
label["foreground"] = "blue"
label["background"] = "yellow"
label["width"] = 20
label["height"] = 3
label["font"] = ("Courier New", 18)
label.pack(padx=10, pady=10, side=tk.LEFT)

button = tk.Button()
button["text"] = "Roll die"
# Link button click to function
button["command"] = start_random
button["width"] = 20
button["height"] = 3
button["font"] = ("Courier New", 18)
button["activebackground"] = "orange"
button["borderwidth"] = 5
button["relief"] = tk.GROOVE
button.pack(padx=10, pady=10, side=tk.RIGHT)

options = {
    "text": "Roll die",
    "command": start_random,
    "width": 20,
    "height": 3,
    "font": ("Courier New", 18),
    "activebackground": "orange",
    "borderwidth": 5,
    "relief": tk.GROOVE
}
button = tk.Button(**options)
button.pack(padx=10, pady=10, side=tk.RIGHT)


options = [
    "hexadecimal",
    "binary"
]
selected = tk.StringVar()
selected.set("hexadecimal")

dropdown = tk.OptionMenu(root, selected, *options)


dropdown.pack()
root.mainloop()
