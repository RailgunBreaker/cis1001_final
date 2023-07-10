# This the function of all of the room.
import model
import random


def KitchenRoom() -> bool:
    """
    This program is to program a game for the group project.
    This is created by Rinka Moriyama
    This is created on June 27th, 2023.

    Room 1: Kitchen
    Returns: True if the player passes this room, false if the player dies in this room. 
    """

# How to make a HP system program: idk how to make player to lose HP if they fail

    model.typeWriterEffect(
        "You are in the kitchen in the submarine. Your mission is to obtain a boiled egg.")

    # Question 1
    model.typeWriterEffect(
        "Question 1: What do you need to make a boiled egg? [gwarge]")
    while True:
        answer1 = input("Please answer from []: ")
        if answer1 == "raw egg" or answer1 == "rawegg":
            model.typeWriterEffect("Correct!")
            break
        else:
            model.typeWriterEffect("Incorrect!")
            model.moveCosts()
            if model.hp <= 0:
                return False

    # Question 2
    model.typeWriterEffect(
        "Question 2: What do you need to make a boiled egg? [atwrtohe]?")
    while True:
        answer2 = input("Please asnwer from []: ")
        if answer2 == "hot water" or answer2 == "hotwater":
            model.typeWriterEffect("Correct!")
            break
        else:
            model.typeWriterEffect("Incorrect!")
            model.moveCosts()
            if model.hp <= 0:
                return False

    # Question 3
    model.typeWriterEffect(
        "Question 3: What do you need to make a boiled egg? [eifr]?")
    while True:
        answer3 = input("Please answer from []: ")
        if answer3 == "fire":
            model.typeWriterEffect("Correct!")
            break
        else:
            model.typeWriterEffect("Incorrect!")
            model.moveCosts()
            if model.hp <= 0:
                return False

    # Question 4
    model.typeWriterEffect(
        "Question 4: What do you need to make a boiled egg? [opt]?")
    while True:
        answer4 = input("Please answer from []: ")
        if answer4 == "pot":
            model.typeWriterEffect("Correct!")
            break
        else:
            model.typeWriterEffect("Incorrect!")
            model.moveCosts()
            if model.hp <= 0:
                return False

    egg = '''
      .-''-.
    .'      '.
   /   .-''-. \\
  /  /       \  \\
  |  ;         | | 
   \  \     .-./ /
    '. `''''''' /
      '-.____.-'
      -> boiled egg in the first lecture of CIS 1001.
'''
    model.typeWriterEffect(egg)
    model.typeWriterEffect("You have obtained a boiled egg.")
    model.inventory[0] = True
    return True


def draw_solar_room():
    """
    Draws an illustration of the solar room. 
    Written by Shuntaro Hori
    """

    room_width = 25
    room_height = 10

    # Draw the top border
    model.typeWriterEffect("┏" + "━" * room_width + "┓")

    # Draw the room walls
    for _ in range(room_height):
        model.typeWriterEffect("┃" + " " * room_width + "┃")

    # Draw the middle divider
    model.typeWriterEffect("┣" + "━" * room_width + "┫")

    # Draw the solar panels
    panel_width = room_width // 2
    panel_height = room_height - 2

    for _ in range(panel_height):
        model.typeWriterEffect("┃" + " " * (panel_width - 4) +
                               "┌────┐" + " " * (panel_width - 4) + "┃")

    # Draw the bottom border
    model.typeWriterEffect("┗" + "━" * room_width + "┛")



def EngineRoom() -> bool:
    """
    Room 2: Engine Room 
    Pass a guess number problem. 
    Written by Yeonkyung Sohn
    """

    model.typeWriterEffect("Your in engine room.")
    model.typeWriterEffect(
        "Now your quest is to obtain the nuclear power! \nTo get the nuclear power, you have to guess the number that computer choose!")

    while True:
        numbers = list(range(1, 5))
        computer_choice = random.choice(numbers)
        user_choice = None
        try:
            user_choice = int(input(
                "Choose a number from 1-5 that satisfy the number that computer choose (Number ONLY)\n>>> "))
        except ValueError:
            print("ENTER IN NUMBER")
            continue
        if user_choice == computer_choice:
            model.typeWriterEffect("Correct! You obtained the nuclear power!")
            model.typeWriterEffect(
                "+--------+ \n| nuclear | \n|  power  | \n+--------+")
            break
        else:
            msg = "Sorry, the correct number was " + \
                str(computer_choice) + ".\n Your HP decreased by 1"
            model.typeWriterEffect(msg)
            model.hp -= 1
            if model.hp <= 0:
                return False

    model.inventory[1] = True
    return True


def SolarRoom() -> bool:
    """
    Room 3: Solar Room

    Returns: True if the player passes this room, false if the player dies in this room. 
    Written by Shuntaro Hori
    """

    draw_solar_room()

    model.typeWriterEffect(
        "Welcome to the solar room, solve a simple puzzle to acquire a Ballast Tank.")
    model.typeWriterEffect("Quiz: What is 1 + 1?")
    answer = int(input("Your answer: "))

    while answer != 2:
        model.typeWriterEffect("Incorrect, try again.")
        model.moveCosts()
        answer = int(input("Your answer: "))
        if model.hp == 0:
            model.typeWriterEffect("You have died.")
            return False

    model.typeWriterEffect("Correct! You have acquired a Ballast Tank.")
    model.inventory[2] = True
    return True

