#learn the tools you need to make your programs perform steps many times,
# and you will apply this by creating an interactive word puzzle.

#LOOP
# An important feature of programs is the ability for the computer to
# repeat certain steps over and over again
# In Python, we tell the program to loop by using either the 'for' or
# the 'while' keyword, depending on our specific situation.

# WHILE LOOP
# an example of some codes that asks the user for payment 
# amount and then displays it back and it works great if the user provides a
# correct value such as 5, but what happens if the user types in a
# negative number? it wouldn't work very well. so we would put something
# in the code to ask them to try again like adding an IF statement like;
#payment = float(input("What is the payment amount? "))

#if payment < 0 :
#    print("Sorry the payment cannot be negetive.")
    
#    payment = float(input("What is the payment amount"))
    
#print(f"The amount is ${payment:.2f}")

# it works very well but what happens if the user types in two negative numbers?
# to solve this problem, we can copy and paste the if statement and put it below.
# But you will have to continue with it if you want and it will make your program long
# So what we need is a way for the program to continue to ask this question as long as
# the payment is < 0. In pythong we can easily do this by changing the word
# IF to WHILE

#payment = float(input("What is the payment amount? "))
#while payment < 0:
#    print("Sorry the payment cannot be negetive.")
    
#    payment = float(input("What is the payment amount"))
#print(f"The amount is ${payment:.2f}")

# one thing about this is that it doesn't check that condition instantenously as soon as the value changes,
# instead it checks it at the end of the loop

#payment = float(input("What is the payment amount? "))
#while payment < 0:
#    print("Sorry the payment cannot be negetive.")
    
#    payment = float(input("What is the payment amount"))
    
#    print("...")
#    print("...")
#    print("...")
#    print("...")
    
#    # it jumps back to while payment < 0:
#print(f"The amount is ${payment:.2f}")

# VARIABLES AND WHILE LOOPS
# In the while loop we asked the user for an amount of payment and also
# see if the amount is negative and as long as or 'while' the payment is
# negative it will keep prompting them for a new value. If for instance
# there's a penalty associated for trying to make a negative payment;

#payment = float(input("What is the payment amount? "))

#while payment < 0:
#    penalty = 1.50
    
#    print("Sorry the payment cannot be negetive.")
#    payment = float(input("What is the payment amount"))

#print(f"The amount is ${payment:.2f}. The penalty is ${penalty:.2f}")

# This looks good but what if the program never enters into the loop?
# there will be no value for the penalty veriable down below, and it will
# display an error message 'penalty is not defined' nd it is a little tricky.
# variables belong to the code block in which they'er first decleared or
# used, this is called their scope that means if you declear a variable
# inside a 'while loop' or a 'function' once you leave that block of code,
# you shouldn't use it anymore even in other languages. So instead if you
# want to use the variable after the while loop block is over, you should
# define it before the while loop starts

#payment = float(input("What is the payment amount? "))

#penalty =  0 # A good default value for the penalty in this case is 0

#while payment < 0:
#    penalty = 1.50
#    
#    print("Sorry the payment cannot be negetive.")
#    payment = float(input("What is the payment amount"))

#print(f"The amount is ${payment:.2f}. The penalty is ${penalty:.2f}")

# This same principle applies to values that you want to use in the
# condition of the 'while loop' as well, so if you decide that you want to
# wait to get the input until after your loop starts, that can work but you
# need to be careful to define your variable first.

# This second example has been simplified to remove the sorry message and
# the penalty amount
#payment = float(input("What is the payment amount? "))

#while payment < 0:
#    payment = float(input("What is the payment amount"))

#print(f"The amount is ${payment:.2f}")

# When you look at the code, you'll see that the code input statement has
# been duplicated and it would be really nice if the amount can be asked for
# once in the loop and then have it run the loop again if it is negative.

#while payment < 0:
#    payment = float(input("What is the payment amount"))

#print(f"The amount is ${payment:.2f}")

# This approach can work but the way it has been written can be a problem it
# will display an error message that 'payment is not defined'. So in this
# case we need to define the payment variable first before the loop so that
# we can check it in the condition

#payment = -1
# what should the payment be set to? it doesn't really matter because its
# going to be overwritten, but we have to make sure that it's going to get
# into the loop, so in this case we are going to make sure it is a negative
# number because if it were a positive value, it would skip right over the
# loop
#while payment < 0:
#    payment = float(input("What is the payment amount"))

#print(f"The amount is ${payment:.2f}")

# The -1 didn't cause any issues it just sat there to get me into the loop.
# and made sure that you can check the condition that you can use the
# variable after. The important thing to remember here is that when you
# first declear and initialize the variable, that determines the code block
# it lives in, you can use it in blocks that are deeper indented than it,
# but you shouldn't try use it in any code blocks that are outside that
# indentation level

# FOR LOOP
# Its very common to have a list of items and to want tot group through
# each item in the list and do something with it. e.g a list of songs on a
# playlist and for each one we might want to list out the artist, the song
# name and include a link to play it. In the example below is a group of
# cities to be displayed. List is defined with [square bracket].
# In python there's a special loop that is used whenever we have something
# to do 'with each' or 'for each' item in a collection and its called a
# "FOR LOOP". The structure of a for loop starts witha a keyword 'for' and
# then pick a variable name to store an individual item called the
# 'iterate variable'.

#cities = ["Asaba", "Abuja", "Awka", "Abia"]

#for city in cities:
#    print(city)
    
# When you starting to use for loops, the iteretor variable can be a little
# hard to get use to. While a list variable is usually a plural noun, your
# iteretor variable should be a singular word because it would represent a
# single item in a list

# FOR LOOPS USING RANGE
# Counting or iterating through a list of numbers is very common in
# programming e.g. displaying a list of search result on a page and put the
# numbers like 1, 2, 3, in front of them. below is how to use 'for loop'
# in counting in python:

#numbers = [1, 2, 3, 4, 5]

#for number in numbers:
#    print(number)
    
# What if we needed a list of over 100numbers, Instead of creating an actual
# list, python can generate an efficient list for us using the range function.
# To use a range function, you specify where to start, stop, and how to
# step through our counting

#numbers = [1, 2, 3, 4, 5]

#for number in range(11): # to count by 2 or 3 we change the step 
    #value to the number
#    print(number)
# Typically you shouldn't use single letter variable names, but for simple
# counting loops like this, it is standard practice to use the letter 'i'
# for your integer variable to count up
#numbers = [1, 2, 3, 4, 5]

#for i in range(11):
#    print(i)

# LOOPING THROUGH STRINGS
# How to itereate and loop through each letter in a string, is just like
# looping through the words and number in a list
# e.g 1thes 5:16
#scripture = "Rejoice evermore."
# Python treats letters in a string just like it does items in a list so
# using a 'for loop' we can iterate them one by one
#for letter in scripture:
#    print(letter)
# This works great but sometimes you want to access the letter by their
# position/ index in the string, this would be useful if you were comparing
# two letters at the same position in two different strings. you can access
# a letter at any index by putting that index in [square brackets]
#scripture = "Rejoice evermore."
#letter = scripture[2]
#print(letter)
# Using this appraoch, if we want it we could now itereate through each
# letter using a 'for i in range' instead of the above example

#scripture = "Rejoice evermore."

#for i in range(17):
#    letter = scripture[i]
#    print(letter)
# This approach works well if you know the lenth of the string, but we can
# get that directly from our program using another built in function in
# python called 'len' short for 'length'

#scripture = "Rejoice evermore."

#scripture_length = len(scripture)

#for i in range(scripture_length):
#    letter = scripture[i]
#    print(letter)

# This can work for scriptures of any length, even if you change the string
# at "Rejoice evermore" you don't have to modify any code at the bottom.
# This turns out to be a common thing to do, so instead of storing it into
# its own veriable on its own line like that above, they do it like;
#scripture = "Rejoice evermore."

#scripture_length = len(scripture)

#for i in range(len(scripture)):
#    letter = scripture[i]
#    print(letter)
