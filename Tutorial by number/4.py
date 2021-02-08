import os #imports the module 'os' for use. This module comes with Python when it is installed.
foo = input("Enter what you want the console to say: ")#We've done this before! Just taking user input and giving it to foo
os.system(str(foo))# This uses the 'system' function in the module 'os'. This will print out whatever the user says in the computer's CMD
print("Should have executed!") #This will not execute if the program fails
