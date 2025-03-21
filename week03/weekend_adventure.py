"""
Text-Based Adventure Game
Creativity Added:
1. A hidden choice in the second level that leads to a secret ending.
2. A trick question in the third level that changes the outcome based on the user's response.
3. The game includes more than two choices in one of the scenarios.
"""

print("Welcome to the Dark Forest Adventure!")
print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")
choice1 = input("Type MATCH or FLASHLIGHT: ").strip().lower()

if choice1 == "match":
    print("\nYou pick up the match and strike it. For an instant, the forest around you is illuminated.")
    print("You see a large grizzly bear, and then the match burns out.")
    print("Do you want to RUN, HIDE behind a tree, or THROW the match?")
    choice2 = input("Type RUN, HIDE, or THROW: ").strip().lower()

    if choice2 == "run":
        print("\nYou start running, but the bear chases you. You trip over a root and fall.")
        print("Do you want to PLAY DEAD or FIGHT the bear?")
        choice3 = input("Type PLAY DEAD or FIGHT: ").strip().lower()

        if choice3 == "play dead":
            print("\nYou play dead, and the bear loses interest. You survive!")
        elif choice3 == "fight":
            print("\nYou try to fight the bear, but it's too strong. Game over!")
        else:
            print("\nInvalid choice. The bear attacks you. Game over!")

    elif choice2 == "hide":
        print("\nYou hide behind a tree. The bear doesn't see you and walks away.")
        print("You notice a hidden PATH leading deeper into the forest. Do you want to FOLLOW it or STAY?")
        choice3 = input("Type FOLLOW or STAY: ").strip().lower()

        if choice3 == "follow":
            print("\nYou follow the hidden path and find a treasure chest! You win!")
        elif choice3 == "stay":
            print("\nYou stay hidden until the bear is gone. You survive, but miss the treasure.")
        else:
            print("\nInvalid choice. The bear finds you. Game over!")

    elif choice2 == "throw":
        print("\nYou throw the match, and it lands in a pile of dry leaves. A small fire starts.")
        print("The bear is scared and runs away. Do you want to PUT OUT the fire or RUN away?")
        choice3 = input("Type PUT OUT or RUN: ").strip().lower()

        if choice3 == "put out":
            print("\nYou put out the fire and save the forest. You are a hero!")
        elif choice3 == "run":
            print("\nYou run away, but the fire spreads. Game over!")
        else:
            print("\nInvalid choice. The fire spreads, and you are trapped. Game over!")

    else:
        print("\nInvalid choice. The bear attacks you. Game over!")

elif choice1 == "flashlight":
    print("\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you.")
    print("You thought you also heard something off to the side.")
    print("Do you want to FOLLOW the path, LOOK in the trees, or SHOUT for help?")
    choice2 = input("Type FOLLOW, LOOK, or SHOUT: ").strip().lower()

    if choice2 == "follow":
        print("\nYou follow the path and find a cabin. Do you want to KNOCK on the door or ENTER quietly?")
        choice3 = input("Type KNOCK or ENTER: ").strip().lower()

        if choice3 == "knock":
            print("\nYou knock on the door, and a friendly hermit invites you in. You survive!")
        elif choice3 == "enter":
            print("\nYou enter quietly, but the hermit mistakes you for an intruder. Game over!")
        else:
            print("\nInvalid choice. You hesitate too long and get lost. Game over!")

    elif choice2 == "look":
        print("\nYou look in the trees and see a pair of glowing eyes. Do you want to THROW a rock or IGNORE it?")
        choice3 = input("Type THROW or IGNORE: ").strip().lower()

        if choice3 == "throw":
            print("\nYou throw a rock, and the creature runs away. You continue safely.")
        elif choice3 == "ignore":
            print("\nYou ignore the eyes, but the creature attacks you. Game over!")
        else:
            print("\nInvalid choice. The creature attacks you. Game over!")

    elif choice2 == "shout":
        print("\nYou shout for help, and a group of hunters hears you. They rescue you and take you to safety.")
        print("Do you want to THANK them or ASK for directions?")
        choice3 = input("Type THANK or ASK: ").strip().lower()

        if choice3 == "thank":
            print("\nYou thank the hunters, and they offer you a place to stay. You survive!")
        elif choice3 == "ask":
            print("\nYou ask for directions, and they guide you out of the forest. You win!")
        else:
            print("\nInvalid choice. The hunters leave you behind. Game over!")

    else:
        print("\nInvalid choice. You get lost in the forest. Game over!")

else:
    print("\nInvalid choice. You stumble in the dark and get lost. Game over!")

print("\nThanks for playing the Dark Forest Adventure!")