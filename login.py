# name_list = ["Ahmad", "Hagar", "Aya", "Wesam", "Doaa"]

# return: username, size
def get_username():
    username = str(input("Enter your username: "))
    size = len(username)
    while size < 5:
        username = str(input("Error your username has to be at least 5 characters "))
        size = len(username)
    return username, size

#return: 1 
def write_name(username, size, name_list = 0):
    with open("data.txt", "a") as data_file:
        data_file.write(username + "\n")
    #size += 1
    # name_list.append(username)
    # name_list.sort()
    return 1

username, size = get_username()

if (write_name(username, size)):
    print("Successfully registerd!")
    print("Welcome " + username + "!")
else:
    print("Error registering your account")







AAAAAAAAAAAAAAAAAAAAAAAAAAAAA = 0











# print("This is new list of users: ", name_list[0:])

# for x in range(int(size)):
#     if name_list[x] == username:
#         print("Your  username is at index", x)

