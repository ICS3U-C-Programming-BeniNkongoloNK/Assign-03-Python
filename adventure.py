#!/usr/bin/env python3
# Created By: Beni
# Date: April 8, 2025
# Takes you on an adventure!

# Imports a time and system(sys) function
import time
import sys


# Defines a 'write' function that makes strings show up letter by letter (Atri helped with this)
def write(str, eol="\n"):
    for char in str:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(eol)
    sys.stdout.flush()
    return ""


def main():

    # Introduces magic ball, and asks for name
    write(
        "Hello! I am a magic ball that rolled into your house! I came since you looked so bored. \nWhat's your name:"
    )
    user_name = input()

    # Asks if you want to play the game
    write("Hello {}".format(user_name) + ". Would you like to play a game? (y/n)")
    answer = input()

    # If you do want to play the game (y)
    if answer == "y":
        # Gives short story
        write(
            "With the first light of dawn painting the horizon, you step outside onto the weathered deck."
        )
        write("The scent of salt and adventure thick in the air.")
        write(
            "Your hands gripped the rope tieing the boat down, eyes fixed on the endless blue stretching ahead."
        )

        # Decide on which item you want to take
        answer = input(
            "Before you depart, you have to make your first choice: \n1. Rifle \n2. Food \n3. Baconator \n(1, 2 or 3) \n"
        )

        try:
            # Converts answer to an integer to save later, changes depending on your answer to the question above(line 38)
            answer_int = int(answer)
            if answer_int == 1:
                write("You take the rifle.")
            if answer_int == 2:
                write("You take the food")
            if answer_int == 3:
                write("You take the Baconator")

            # More lore!
            write(
                "Days into your voyage, the calm was shattered by black sails on the horizon, cutting through the waves like blades."
            )
            write(
                "The pirates closed in fast, their cannons booming and voices wild with the thrill of the chase."
            )

            # Ask if you want to fight the pirates or run away
            answer = input(
                "Quickly, you must choose whether you wish to fight or flee! (fight/ flee)\n"
            )

            # If you chose to fight check if you have the baconator. If so you win!
            if answer == "fight":
                if answer_int == 3:
                    write(
                        "You are victorious! Your Baconator distracted the enemies with it's delicious taste and gave you the opportunity to stike!"
                    )
                    write("As you sit in you think 'what a mighty victory!")
                    write(
                        "Good job {}".format(user_name)
                        + ", I hope this little game made you less bored. Play it again for the other endings!"
                    )

                elif answer_int == 2 or answer_int == 1:
                    write(
                        "You are unprepared for the fight. You try your hardest but simply cannot beat the willpower of the pirates"
                    )
                    write("Eventually they swarm you, and you are defeated")
                    write(
                        "Unlucky {}".format(user_name)
                        + ", I hope this little game made you less bored. Play it again for the other endings!"
                    )
                else:
                    write(
                        "Sorry! That's not a valid input. Play the game again; correctly this time!"
                    )

            # If you chose to run check if you have the rifle. If so you win!
            elif answer == "flee":
                if answer_int == 1:
                    write(
                        "The pirates show off their shiny swords, but shake in fear and awe of your modern rifle. However, you are a pacifist and choose not to fight"
                    )
                    write(
                        "The pirates are inspired by your choice and turn a new leaf, never to fight again!"
                    )
                    write("As they sail away you shoot them all down!")
                    write(
                        "Good job {}".format(user_name)
                        + ", I hope this little game made you less bored. Play it again for the other endings!"
                    )
                elif answer_int == 2 or answer_int == 3:
                    write(
                        "Your attempts at escape are futile, their ships are far faster than yours. They capture you!"
                    )
                    write(
                        "With your last breath you yell for help. But there is no savior in the ocean."
                    )
                    write(
                        "*The next actions cannot be said as this is a school assignment!!!!*"
                    )
                    write(
                        "Unlucky {}".format(user_name)
                        + ", I hope this little game made you less bored. Play it again for the other endings!"
                    )
                else:
                    write(
                        "Sorry! That's not a valid input. Play the game again; correctly this time!"
                    )

        except:
            write("Sorry that was an invalid input. Play the game right next time!!")

    elif answer == "n":
        write("Alright, your choice. Bye bye!")
    else:
        write("Sorry that's an invalid input")


if __name__ == "__main__":
    main()
