# This the main function of the program
import sys
import model
import SavaGame
import Rooms
"""
This function is written by Guohua.S
"""
room = 1
rooms = [Rooms.KitchenRoom, Rooms.EngineRoom, Rooms.SolarRoom]

submarine = '''
      |_
   _____|~ |____
  (  --         ~~~~--_,
   ~~~~~~~~~~~~~~~~~~~'`   

Escape from undersea
'''
def main():
    global room, rooms, submarine
    
    model.typeWriterEffect(submarine)
    model.typeWriterEffect(
        "Weclome to Escape from undersea, this is an escape room game that the requirement of escaping from a leaking submarine.")

    # name of player
    char_name = input("\nWhat's your name?\n>>> ")
    model.typeWriterEffect("Hello " + char_name + "! Welcome to the game!")

    # introduce background story
    backgroundStory = "\nYou are a renowned deep-sea explorer, known for your courage and resourcefulness.\nThis time, you board a submarine and embark on a journey to explore the wreckage of a sunken ship.\nHowever, you receive a distress signal from a submarine in trouble.\nIT IS SINKING!\nYour mission is to FIND THREE IMPORTANT ITEMS: a boiled egg, backup nuclear power, and backup ballast tanks.\nExplore the submarine, solve puzzles, and overcome obstacles to prevent a disaster at the bottom of the ocean.\nTime is running out, so act quickly and courageously to succeed in your mission!"
    model.typeWriterEffect(backgroundStory)

    model.typeWriterEffect(
        "\nWarm Tip! You will minus 1 hp for every stupid action, you have 20 hp in total!")

    """
    This function is written by Heying Liu
    Modified by Guohua.S
    """
    # main room loop
    while True:
        model.typeWriterEffect(
            "Available options:\n\tCheck HP (H)\n\tCheck Inventory (I)\n\tEnter Next Room (R)\n\tSave Game (S)\n\tLoad Game (L)\n\tExit Game(E)")
        userAction = model.askInputUntilValid(
            ">>> ", "H", "I", "R", "S", "L", "E" "h", "i", "r", "s", "l","e", "Check HP", "Check Inventory", "Enter Next Room", "Save Game", "Load Game", "Exit", "exit")

        if userAction.lower() == "h" or userAction == "Check HP":
            model.plotHealthBar()
        elif userAction.lower() == "i" or userAction == "Check Inventory":
            msg = ""
            for i in model.getCurrentInventory():
                msg += (i + ", ")
            model.typeWriterEffect(msg)
        elif userAction.lower() == "r" or userAction == "Enter Next Room":
            rooms[room - 1]()
            room += 1
        elif userAction.lower() == "s" or userAction == "Save Game":
            SavaGame.saveGame(char_name)
        elif userAction.lower() == "l" or userAction == "Load Game":
            savedRoom = SavaGame.loadGame(char_name)
            if savedRoom >= 0:
                room = savedRoom + 1
        elif userAction.lower() == "e" or userAction == "Exit" or userAction == "exit" or userAction == "E":
            sys.exit()
                

        # check if the game is over
        if model.isGameOver() < 0:
            model.typeWriterEffect("You have lost all your HP. Game over.")
            break
        elif model.isGameOver() > 0:
            model.typeWriterEffect(
                "You have obtained all three inventory items. You have escaped the submarine.\nCongratulations!")
            break
        else:
            # seperator
            model.typeWriterEffect("\n" + "-" * 50 + "\n")

while True:
    main()
    again = model.askInputUntilValid("Are you sure to exit?\nYour game will not be saved\nPress Enter to play again, or type 'exit' to quit the game.\n>>> ", "exit", "Exit", "")
    if again.lower() == "exit" or again.lower() == "e" or again.lower() == "quit" or again.lower() == "q":
        break
    elif again == "":
        model.resetGame()
        room = 1