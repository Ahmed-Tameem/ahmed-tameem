# return: username, size
def get_info():
    username = str(input("Enter your username: "))
    user_size = len(username)
    while user_size < 5:
        print("Your username has to be at least 5 characters!")
        username = str(input("Try another username: "))
        user_size = len(username)

    password = str(input("Enter your password: "))
    password_size = len(password)
    while password_size < 5:
        ("Your password has to be at least 5 characters!")
        password = str(input("Try another password: "))
        password_size = len(password)  

    return username, password

#return: 1 
def write_info(username, password):
    with open("data.txt", "a") as data_file:
        data_file.write(username + "\t")
        data_file.write(password + "\n")
    return 1

# class user:
#     username
#     password



username, password = get_info()

if (write_info(username, password)):
    print("Successfully registerd!")
    print("Welcome " + username + "!")
else:
    print("Error registering your account")