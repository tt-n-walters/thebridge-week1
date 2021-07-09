import tkinter as tk


def decode_from_binary(binary):
    binary_list = binary.split()
    characters = []
    for i in range(len(binary_list)):
        binary = binary_list[i]
        n = int(binary, base=2) - 10
        char = chr(n)
        characters.append(char)

    message = "".join(characters)
    return message


def encode_to_binary(message):
    binary_list = []
    for i in range(len(message)):
        char = message[i]
        n = ord(char) + 10
        # binary = bin(n)
        binary = format(n, "b")
        binary_list.append(binary)
    
    binary = " ".join(binary_list)
    return binary


def decode_from_hexadecimal(hexadecimal):
    hex_list = hexadecimal.split()
    characters = []
    for i in range(len(hex_list)):
        hexa = hex_list[i]
        n = int(hexa, base=16)
        char = chr(n)
        characters.append(char)
    message = "".join(characters)
    return message


def encode_to_hexadecimal(message):
    hex_list = []
    for i in range(len(message)):
        char = message[i]
        n = ord(char)
        hexa = hex(n)
        hex_list.append(hexa)
    hexadecimal = " ".join(hex_list)
    return hexadecimal


root = tk.Tk()


def encode_text():
    message = text_input_1.get("1.0", tk.END).strip()
    encoded = encode_to_hexadecimal(message)
    text_input_2.insert("1.0", encoded)
    text_input_1.delete("1.0", tk.END)


def decode_text():
    encoded = text_input_2.get("1.0", tk.END)
    message = decode_from_hexadecimal(encoded)
    text_input_1.insert("1.0", message)
    text_input_2.delete("1.0", tk.END)


def handle_keypress(event):
    if event.keycode == 13:
        encode_text()


# Create widgets
options = {
    "font": ("Consolas", 14)
}
top_frame = tk.Frame()
text_input_1 = tk.Text(top_frame, **options)
button_1 = tk.Button(top_frame, **options)

text_input_1.bind("<Key>", handle_keypress)

bottom_frame = tk.Frame()
text_input_2 = tk.Text(bottom_frame, **options)
button_2 = tk.Button(bottom_frame, **options)


# Widget customisation
text_input_1["width"] = 40
text_input_1["height"] = 6

button_1["command"] = encode_text
button_1["text"] = "Encode"

text_input_2["width"] = 40
text_input_2["height"] = 6
button_2["command"] = decode_text
button_2["text"] = "Decode"


# Pack widgets
text_input_1.pack(side=tk.LEFT)
button_1.pack(side=tk.LEFT)
top_frame.pack(padx=10, pady=10)

text_input_2.pack(side=tk.LEFT)
button_2.pack(side=tk.LEFT)
bottom_frame.pack(padx=10, pady=10)

root.mainloop()
