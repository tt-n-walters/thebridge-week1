print("Welcome to the most wonderful page ever.")
attempts = 0
while True:
  print("Enter username:")
  username = input()
  if username == "nico.walters":
    print("Enter password:")
    password = input()
    if password == "password1":
      print("Access granted.")
      break
    else:
      print("Incorrect password.")
      print("You have", 2 - attempts, "tries remaining.")
      attempts = attempts + 1
    if attempts == 3:
      print("Account locked.")
      break
  else:
    print("Invalid username.")