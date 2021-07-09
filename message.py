binary = "01110000 01111001 01110100 01101000 01101111 01101110 00100000 01101001 01110011 00100000 01110111 01101111 01101110 01100100 01100101 01110010 01100110 01110101 01101100"

hexa = [0x74, 0x65, 0x63, 0x68, 0x74, 0x61, 0x6c, 0x65, 0x6e, 0x74, 0x73, 0x20, 0x32, 0x30, 0x32, 0x31]


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
    
message = input("Enter message: ")
encoded = encode_to_binary(message)

print(decode_from_binary(encoded))