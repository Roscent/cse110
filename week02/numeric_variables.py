"""# A variable with quotation marks are strings
# while a variable without quotation marks are numbers and you cant use letters in a integer
# you cannot mix strings and numbers together in a math operation in python
# maths requires all numbers
#
song1 = "213 seconds" #this is a string
song2 = 213 # this is a number (int)
song3 = 213.5 # this is a number (float)
song4 = "150"
song5 = "250.25"

playlist = song4 + song5
print(f"The playlist is {playlist} seconds.")
"""

#CONVERTING STRINGS TO NUMBERS
#Converting data from one type to another is called type-casting, or "casting."
"""song1 = 162
song2 = 175
song3 = input("What is the length of the song? ")

song3_input = int(song3)

playlist = song1 + song2 + song3_input

print(f"The playlist has {playlist} seconds")

song1 = 162
song2 = 175
song3 = int(input("What is the length of the song? "))

#song3_input = int(song3)

playlist = song1 + song2 + song3

print(f"The playlist has {playlist} seconds")

# This creates a new integer variable with the value of 10
# There is nothing magical about the "_num" in the variable name, it will just
# help us keep track of it
length_num = 50
width_num = 10

# If you add the numbers together, you would get the result you expect:
print(length_num + width_num) # This displays: 60

# You can convert the values to the strings "50" and "10" like this:
length_string = str(length_num)
width_string = str(width_num)

# The computer now thinks of these variable as two characters, the digit 5 followed
# by the digit 0, and the digit 1 followed by the digit 0.

# If you try to add the two strings together, it will concatenate them, or display
# one after the other:
print(length_string + width_string) # This displays: 5010
# Whenever you get input from the user using input, it will be a string by default:
quantity_from_user = input("How many items do you have? ")

# The variable quantity_from_user is a string.
# To convert it to an integer you use the int(...) notation:
quantity_number = int(quantity_from_user)

# Because the quantity_number variable is an integer you can do math with it:
double_number = quantity_number * 2

# If you want to use these values in strings, you CANNOT just add them, you first
# have to convert them to a string:

# WRONG:
print("Twice as many is: " + double_number)

# Right:
double_string = str(double_number)
print("Twice as many is: " + double_string)

# You can also do this in one step:
# Right:
print("Twice as many is " + str(double_number))
#Similar to the last example, you can combine the input and int commands into one line:
# Using two lines:
people_string = input("How many people are in the room? ")
people_number = int(people_string)

# Using one line:
people_number = int(input("How many people are in the room? "))

# The same works for floating point numbers:
length_number = float(input("What is the length? "))
"""

"""#ADDING A DECIMAL VALUE TO THE INPUT GIVE AN ERROR
# WE CHANGE THE int IN SONG3 TO float
song1 = 162
song2 = 175
song3 = float(input("What is the length of the song? "))

#song3_input = int(song3)

playlist = song1 + song2 + song3

print(f"The playlist has {playlist} seconds")
#there's no problem mixing int and float if you do,
# Python will just do the math and give you the result as a float
"""

#CONCATENATE
"""color = 'blue'
animal = 'horse'

# You can add, or concatenate, two strings together with +:
print(color + animal)
# This displays: bluehorse

# You can add many strings together, whether the strings are variables or directly in
# the quotation marks:
print(color + ' ' + animal + '!')
# This displays: blue horse!

# You can also save the result into a new string variable:
combined_words = color + ' ' + animal + '!'
print(combined_words)
#On the other hand, if the data type of the variables is integer or floating
#point, the + operator actually performs the mathematical addition:
boys_count = 10
girls_count = 12

# Add two numbers together using the + operator:
print(boys_count + girls_count)
# This displays: 22

# You can save the result in a new variable to use later:
total_count = boys_count + girls_count
print(total_count)
"""

"""#Mixing Strings and Numbers
apple_count = 5

# Error on this line... You can't add strings and integers together!
print("You have " + apple_count + " apples") # ERROR!
"""

#Expressions and Mathematical Operations
#Once you have numeric values stored in variables, you can perform a
#variety of complex mathematical operations. The following are
#common mathematical operators in Python:
"""Operator	        Symbol	Example	Result

Add                    +     3 + 4      7

Subtract               -     3 - 4      -1

Multiply               *     3 * 3      12

Divide                 /     15 / 4     3.75

Divide and             //    15 // 4    3
drop remainder

Remainder or            %    25 % 7     4
Modulus
(Get the remainder
 that would result
from dividing the 
first number by
the second one.)

Exponent                **      3 ** 4     81
(To the power of)
"""

# These operators follow standard mathematical orders of operation
# (where * happens before +), but you can force it to evaluate using
# parentheses. For example, (3 + 4) * 2 will perform the addition first,
# and then multiple the result by 2.

x = 2
y = 3
z = 4  

w = x + y * z  

print(w)