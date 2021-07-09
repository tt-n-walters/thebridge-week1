# counter = 0
# while counter < 5:
#     print("Hello world!")
#     counter = counter + 1


# for counter in range(5):
#     print("Hello world!")


# size = 7
# for i in range(size):
#     print("x " * (size - i))

size = 12
for i in range(size):
    for j in range(size):
        if (i + j) % 2:
            print("-", end=" ")
        else:
            print("x", end=" ")
    print()
