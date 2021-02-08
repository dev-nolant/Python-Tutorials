# Taking A User input
# Using the word 'input' not only can replace the function 'print' and require the use to press 'enter' on their keyboard, but can also be used to take a user input
#--------------------------------------------------------------
#<Example>
foo = input("Enter your name: ") #The variable 'foo' will be used and be set whatever value is input for the persons name!
#   So the outcome will be something like "Hello {{foo}}!"              We can use the simple print to display that.
print("Hello "+foo+"!")#This prints 'Hello' and then this is where it can get tricky! To add a string to another set of strings or long string, you can use '+' to combine the strings! 
# In this instance you can see that we added 'foo' to the string 'Hello' and then the string '!' after the variable 'foo'
# It is recommended, to avoid any errors, that we turn anything that foo is set to into a string! Easily done by adding str() to it.
# That would look like >> str(foo) >> and complete it would be >>      print("Hello "+str(foo)+"!")
