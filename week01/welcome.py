"""
BASIC PRINT
print("Welcome to cse110!")
print()
print("This is going to be a great course.")

VARIABLE
name = "Bob"
age = 24

print(name)
print(age)

age = 34
print(age)


THE DEBURGGER
    The red dot is used to set a break point at a line when you want to debug
        and you use the drop down close to the play icon to select DEBUG PYTHON FILE
        in order to start debugging line by line till it gets to the red dot
name = "Peter"
age = 24

print(name)
print(age)


BASIC F-STRINGS
    f-string is also called format string
name = "Bob"
age = 24

print(name)
print(age)

    f-string makes it nicer, it comes before the quotes

print(f"Your name is {name})
    Because we put the f before the quotes, it starts to look for the curly braces
        so that it will print the word in the curly braces
        f-strings works with both words and numeric variable
print(f"Your age is {age})
print(F"Hello {name}, you are {age} years old)


INPUT
    This shows how to get information from a user either a location or color or any kind of information'
place = "Asaba"
print(f"You are from {place})
    If you want to ask the user to input words by themselves we use the INPUT function'
        when you call a function, you write the function and put parentheses in front of it'
place = input("Where are you from? ")
vacation = input("Where do you want tot go on vacation? ")

print(f"You are from {place})
print(f"You want to go to {vacation})

color = input("What is your favorite color? ")
print(f"Your favorite color is {color})
"""



"""
    Input and Output
        COMMENT
            This is used to take notes in python that you don't want to run
                it can either be displayed using '#' or 'three double quotes """""" and write inbetween'
        
        STRING METHODS
            This changes the way string variables is displayed e.g converting
                a user email address to all lowercase or capitalizating all variables or capitalizing the starting of each string
                to conver an email to all lowercase;
email = input("What is your email address? ")
print(email.lower())
            .lower doesn't change the variable permanently
print(email)
            if we want to change it permanently we need to reassign the variable like;
email = email.lower()


            Asking a user for the name of a book
book = input("What's the title of the book? )
            To print it out in all uppercase we do it like;
print(book.upper())
            To print it out with only the first letter capitalized we do it like;
print(book.capitalize())
            To capitalize each word in a title we do it like;
print(book.title())
            if you want to use a string method inside an f-string include it in all the curly braces like;
print(f"The title is: {book.title()}")
"""

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print(f"Your name is {last_name}, {first_name} {last_name}")
print(f"Your name is: {last_name.title()} {first_name.title()} {last_name.title()}")