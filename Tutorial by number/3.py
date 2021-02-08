# We'll now take a look at basic input handling! This program we'll make the user have to input two numbers and we will multiply them!
num1 = input("Enter your first number: ")#We've already learned this, but now we're setting different variables. Like in this case we're using 'num1'
#^ instead of foo like the last one
num2 = input("Enter your second number: ")
#We can have a variable solve the question, then print the variable like so:
answer = int(num1) * int(num2) # '*' is the equivalent to the multiplication symbol in math! :: IMPORTANT -- You must include 'int' - This lets the multiplication know
#that its multiplying intigers and not strings, you are unable to multiply strings by another string.
#answer will now be what num1 times num2 is!
print(answer) #and now we print it! This will print the answer to num1 * num2!! :: IMPORTANT -- 'print' can print 'booleans/bools' which print out 'True/False', intigers,
#and strings, which are any language in quotations or readable. Such as str(1), '"Hello World"', or str(True)
#The attachment 'str()', converts anything inside of the parenthases into a string, unless it's unable to and it will show an error when executed.
