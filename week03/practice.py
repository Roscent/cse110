##IF STATEMENT
## Consider a program that ask the user for their temperature an then
# #Tell them if they should go to the hospita or do something else

#temperature = float(input("What is your temperature in degrees celcius? "))
#if temperature > 40.5:
#    print("Go to the hospital!")
## If you want the program to give a different meesaage if they
## don't need to go to the hospital, we can add a else statement for an easier way
#elif temperature > 39.4:
#    print("Call your doctor.")
#else:
#    print("Consider rest or medicine.")
## If you need to call your health care provider if your temperature is over 39.4 degrees 
## celcius we could consider putting another if statement inside 
## else block it will work, but there's a clear and easier
## way to handle it by adding an 'elif' keyword after the if code block
#print("Have a good day.")


#COMPARING STRINGS
#When your program uses input that comes from the user such as
# email address or password, you'll need to decide does thsi need to match exactly? 
# such as the password, or is this the situation were upper and lower case don't matter.
# We have a program that ask the user for the name of an animal and then it trace to figure
# out what sound it makes then displays back to them.

#animal = input("What is your favourite animal? ")
#animal_lc = animal.lower()
#sound = ""

#if animal_lc == "cat":
#    sound = "meow"
#elif animal_lc == "dog":
#    sound = "ruff"
#else:
#    sound = "unknown"
#print(f"The {animal} makes the sound {sound}.")

# When you use a diiferent case aside the one used to input,
# it will not display the correct feedback so you need to add a case code 
# to fix it that no matter the case be it upper or lower case it will not affect the output
# you acn use this method if animal == "cat" or animal == "Cat" or animal == "CAT": but it will be too 
# long and you'll have to account for each word. 
# you can stil add a .lower or .upper at the front of the word 
# but a better approach is to covert it once at the beginning

#BOOLEAN EXPRESSION
# Any combination of variables and operators is called an expression, 
# we can evaluate an expresion by following the rules of the operators 
# until we get a single value result. most expressions are math esxpressions.
# they use operators like plus and minus and result in a number, but if the expression uses
# operations like = or < to evaluate the true or false, we call them boolean expressions.
# named after George bool and english mathimatician. e.g
""" a game that needs at least seven players to start the game, and at least 
4 women, the program asks for the user to give the number of men and women that are playing
and computes the total number of player. so we will check if the total number are equal or
greater than 7 and if the number of women are greater than or equal to 4
""" 
men = int(input("How many men are there? "))
women = int(input("How many women are there? "))

total = men + women

if total >= 7 and women >= 4:
    print("You can play!")
else:
    print("You cannot play a legal game.")
    
"""if only one of the conditions needs to be true we could use an or operator instead
    """