names = []

while True:
    n = input("Enter name: ")

    if not n:
        break

    # Add the n to the list of names
    names.append(n)
    print(names)

names.sort()
print(names)

print(names[3])