
def read_user_data():
    # step 1 - open the file
    file = open("users.txt", "r")
    # step 2 - access the file (read/write)
    contents = file.read()
    # step 3 - close the file
    file.close()

    lines = contents.splitlines()
    return lines


def process_usernames(lines):
    usernames = []
    passwords = []
    for counter in range(len(lines)):
        line = lines[counter]

        if counter % 2 == 0:       # username
            usernames.append(line)
        else:                      # password
            passwords.append(line)
    return usernames, passwords

def get_username():
    user = input("Enter username: ")
    return user


def get_password():
    password = getpass.getpass("Enter password: ")
    return password


def check_username(usernames, user):
    if user in usernames:
        user_index = usernames.index(user)
        return user_index


def check_password(passwords, user_index, password):
    if password in passwords:
        password_index = passwords.index(password)
        if user_index == password_index:
            print("Login successful.")
            logged_in = True
            return logged_in


def track_attempts():
    pass


# FILE READING

# USERNAME PASSWORD PROCESSING


import getpass

data = read_user_data()
usernames, passwords = process_usernames(data)

# LOGIN SYSTEM CATCH YAH LATER MAH BROTAH
logged_in = False
while logged_in == False:
    username = get_username()

    user_index = check_username(usernames, username)
    if user_index is None:
        print("User not found.")
        continue

    for i in range(3):
        password = get_password()
        logged_in = check_password(passwords, user_index, password)

        if logged_in:
            break
        else:
            print("Incorrect password.", 2 - i, "attempts left.")
    else:
        print("Account locked. Please try again in 24 hours.")


