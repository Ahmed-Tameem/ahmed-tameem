# class user:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def get_info(self):
#         self.username = str(input("Enter your username: "))
#         user_size = len(self.username)
#         while user_size < 5:
#             print("Your username has to be at least 5 characters!")
#             self.username = str(input("Try another username: "))
#             user_size = len(self.username)

#         self.password = str(input("Enter your password: "))
#         password_size = len(self.password)
#         while password_size < 5:
#             print("Your password has to be at least 5 characters!")
#             self.password = str(input("Try another password: "))
#             password_size = len(self.password)

#     def write_info(self):
#         with open("data.txt", "a") as data_file:
#             data_file.write(self.username + "\t")
#             data_file.write(self.password + "\n")
#             print("Welcome " + self.username + "!")
#             print("You are now successfully registerd!")

# my_user = user(None,None)

# while True:
#     my_user.get_info()
#     my_user.write_info()



from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text = "Username").grid(row = 0, column = 0, sticky = W, padx = 4)
Entry(root).grid(row = 0, column = 1, pady = 4)

Label(root, text = "Password").grid(row = 1, column = 0, sticky = W, padx = 4)
Entry(root).grid(row = 1, column = 1, pady = 4)

Button(root, text = "Submit").grid(row = 3, column = 0)

root.mainloop()



