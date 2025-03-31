# # LIST
# # In python we can creat a list variable using brackets, so if you want to
# # keep track of your clients you can creat a new list variable

# clients = [] # this creats an empty list, 
# # But if you want tostart the list with an initial value i can add them 
# # into the square bracket separated by comments;
# clients = ["John", "Mary"] # the square bracket notation is short for a
# # longer way of writing it which could be
# clients = list() # Using square bracket is generally the prefered way of 
# # creating a list, but because is a keyword, if you try to name your variable list like
# list = [] # you'll run into problems, so its better to think about what kind
# # of items you'll be storing in the list and name the list 
# # something that describes it e.g (clients, players, records).
# # Another thing to keep in mind for variable names is because list will
# # stored more than one item it is considered good practice to choose a
# # plural noun with an 's' rather than just calling it with the singular
# # name

# clients = [] # if you want to add clients to this list, you can do so with
# # the append method like;
# clients.append() # Remember that a method is a function that can be used
# # directly on avariable, while append is a list method which can be used on
# # a list variable by putting it after the variable name and a ".(DOT)" and
# # then inside the parenthesis you can include the client you want to add
# clients.append("Roscent")
# clients.append("Nkemjika")
# clients.append("Ofuonye")

# print(clients)

# # So if i want to print my list without the square brackets and one thing 
# # at a time i can use a forloop

# clients.append("Roscent")
# clients.append("Nkemjika")
# clients.append("Ofuonye")

# for client in clients:
#     print(client)
    
# # so why do i use the append instead of putting the names into the bracket 
# # directly? including them directly in a square bracket only works if i
# # know those values when i write thee code, its more likely i'll be getting
# # those values from the user or database and i might be getting them one at
# # a time in which case using append will be easier

# clients.append("Roscent")
# clients.append("Nkemjika")
# clients.append("Ofuonye")

# new_client = input("New client name: ")
# clients.append(new_client)

# for client in clients:
#     print(client)

# LOOPS AND LISTS
# Loops and Lists work solo together that it is almost impossible to talk
# about one without the other. Talk about how to use a list to get value
# from the user and add them to a list;

# clients = []

# print("The clients are: ")
# for client in clients:
#     print(f" {client}") # This code creats an empty list of clients and
#     # use a for loop to iterate through them to display each one, LOOPS are
#     # often use to iterate through a list, display or do something else for
#     # each item. we can also use the loop to ask the user for clients and
#     # add them to the list in this case i could keep asking them for clients
#     # as long as they do not type the word QUIT;
# clients = []
# new_client = "" # New client variable set to an empty quote
# while new_client != "quit": # Checks if the new_client is equal to quit so
#     #that they can stop the loop
#     new_client = input("New client name: ")
#     clients.append(new_client)

# print("The clients are: ")
# for client in clients:
#     print(f" {client}")
    
# # To use quit to stop the loop and not put it in the list, we can also use
# # an IF statement;
# clients = []
# new_client = ""
# while new_client != "quit":
#     new_client = input("New client name: ")
#     if new_client != "quit":
#         clients.append(new_client)

# print("The clients are: ")
# for client in clients:
#     print(f" {client}")

# # Technically, you can mix types of variables and have a list that contains
# # different types of variables (e.g., strings and numbers), but it often
# # makes it harder to work with the list later, so that is generally
# # discouraged. Instead, make a list that has a clear purpose and put only
# # those things in that belong. Then, if needed, make another list for other
# # things.


# # LISTS OF NUMBERS
# # One of the nice things about collections or list in python is that you
# # can put variables of any type in them, you generally want to be careful
# # and not put two different type of variables like strings and numbers into
# # the same list because it makes it hard to know wat to expect when you
# # iterate through it later, but assuming you have a list of numbers there
# # are a lot of things that you might want to do with them later such as find
# # the largest number, the total, or other values. this code contains a list
# # of numbers that could be the amount of points a basket ball player has
# # scored in his ast several games, as an example lets use a loop to add up
# # all of this values and determine the total point scored. Firstly is to
# # iterate through each value in the list using a forloop

# # points_scored = [24, 18, 31, 42, 28]

# # for point_amount in points_scored: # want to add them to a running total 
# #     # that i can start from zero.
# #     running_total = 0 # But if i put this in my loop like this it will 
# #     #create a problem because it will get set back to zero at the start of
# #     # each loop. instead we will put it up b4 the loop in that way it won't
# #     # get reset each time
    
# points_scored = [24, 18, 31, 42, 28]

# running_total = 0
# for point_amount in points_scored:
# # Now each time through the loop, i want to update the running total to be
# # whatever it was b4 + the current amount
#     #running_total = running_total + point_amount
    
# print(f"The player has scored {running_total} points")
# # Because its very common to want to add another value unto a running total
# # like this python and most other languages have a special operator for it
# # the "+=" operator. the += operator works by writing;
#     running_total += point_amount # With the += operator it kinda sqiches
#     #the two running total variable together and put them both on the left
#     # side. This two lines of code 
#         # #running_total = running_total + point_amount
#         # running_total += point_amount
#     # does the exact same thing. so you can use anyone you'er comfortable
#     # with but as you do get more comfortable with programming you'll find
#     # that "running_total += point_amount" is pretty nice and clean.
# # This program computes the total but you could imaging following the
# # similar pattern to compute the average or find the highest amount of
# # point_scored or number of other task by defining variables b4 the loop,
# # they get updated during each iteration.
# # In python there are built in funtions that could accomplish many of this
# # task such as getting the total of a list. But its important to understand
# # this approach because its a pattern that you'll use in a different
# # situation where there may not be a built in function for exactly what you
# # need.

# #LIST INDEXES
# # In this activity, you'll learn how to access items in a list at any
# # location, and also how to remove items.
# # When we work with List in programming, it is important to understand a
# # little bit about how they'er stored in the memory. In python each item in
# # a list has a position in memory that we can access through what's called
# # the INDEX. INDEXES always starts with 0 and count up by 1 for each item
# # in the list
# # index =   0       1       2       3
# colors = ["red", "green", "blue", "yellow"]
# # If you want to access an item in a list by its index, i can use a [] to
# # tell the computer to go to that index location and get the data there,
# # so the item in index one can be printed like;
# print(colors[1]) # we can iterate through the items in a list using a for
# # loop like;

# # index =   0       1       2       3
# colors = ["red", "green", "blue", "yellow"]
# for color in colors:
#     print(color) # But sometimes its helpful to do this using the index,
#     # by using the "for i in range" style of loop like;
# for i in range(len(colors)):
#     color = colors[i]
#     print(color) # In this case they'll take on the value that represents
#     # the index. because looking at our code len is a function that gives me
#     # the length of the list or number of items in the list and range creates
#     # collections from 0 up to but not including the number that length
#     # returns which is 4 in this case because there are four items in the
#     # list. so this loop will iterates through all the indexes needed
# # When using [] to access items in a list, i'll often see something like
# # "colors at i" to remind me that i'm accessing the item at the index 'i'.
# # so colors at 'i' will access the item at the index of 'i' and remember
# # the loop is changing the value of 'i' each time it iterates or starts
# # over

# # index =   0       1       2       3
# colors = ["red", "green", "blue", "yellow"]

# for i in range(len(colors)):
#     color = colors[i]
#     print(color)
    
# # If you want to display a number next to each colors, lets first print
# # the index next to the color using an "fstring"

# # index =   0       1       2       3
# colors = ["red", "green", "blue", "yellow"]

# for i in range(len(colors)):
#     color = colors[i]
#     print(f"{i} . {color}")
    
# # This prints the index which starts at 0, so to change it to start
# # counting from 1 for human use(count) this is always 1 more than the index.
# # lets add a variable above the print statement.

# # index =   0       1       2       3
# colors = ["red", "green", "blue", "yellow"]

# for i in range(len(colors)):
#     color = colors[i]
#     human_count = i + 1
#     print(f"{human_count} . {color}")
    
# # you can remove a certain item or insert it into a list at a certain place
# # e.g to remove the colored index 1, you can pop it off the list by using
# # the "pop" list method and also insert things.
# # In other to use pop we need the name of our list (colors) the add the pop
# # method

# # index =   0       1       2       3
# colors = ["red", "green", "blue", "yellow"]

# colors.pop(2)
# for i in range(len(colors)):
#     color = colors[i]
#     human_count = i + 1
#     print(f"{human_count} . {color}")
    
# # Similarly we can insert at our index too by using the insert method,
# # telling it where to insert and what to insert

# # index =   0       1       2       3
# colors = ["red", "green", "blue", "yellow"]

# colors.insert(2, "lemon")
# for i in range(len(colors)):
#     color = colors[i]
#     human_count = i + 1
#     print(f"{human_count} . {color}")