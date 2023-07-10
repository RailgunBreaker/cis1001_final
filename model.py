# This is the system of the game(hp, win/lose condition)
import matplotlib.pyplot as plt
import time

hp = 20
inventory = [False, False, False]
fullInventory = ["Boiled Egg", "Backup Nuclear Power", "Backup Ballast Tanks"]
figure = None


def plotHealthBar() -> None:
    """
    Plots a health bar with the current health
    Guohua.S
    """

    global figure

    # close the previous figure
    plt.close(figure)
    figure = plt.figure(figsize=(5, 2))

    # plot the health bar
    plt.plot([0, 20], [0, 0], color='red', linewidth=20)
    plt.plot([0, hp], [0, 0], color='green', linewidth=20)
    plt.title("Current Health: " + str(hp))
    plt.axis('off')
    plt.show(block=False)


def moveCosts() -> None:
    """
    Minus 1 hp from the player as a move cost, and plot the health bar. 
    Guohua.S
    """
    global hp
    if hp > 0:
        hp -= 1
        plotHealthBar()
    else:
        pass


def askInputUntilValid(prompt, *validOptions) -> str:
    """
    Asks user for input until it is valid.
    Returns the valid input.
    Heying.L
    """

    while True:
        usrInput = input(prompt)
        if usrInput in validOptions:
            return usrInput
        else:
            typeWriterEffect("Invalid input. Please try again")


def isGameOver() -> int:
    """
    Returns negative if the player has lost all HP. 
    Returns positive if the player has obtained all three inventory items. 
    Returns 0 if the game is not over.
    Sihan.W
    """

    global hp
    if hp <= 0:
        return -1
    elif inventory[0] and inventory[1] and inventory[2]:
        return 1
    else:
        return 0


def getCurrentInventory() -> list:
    """
    Returns the current inventory
    """
    currentInventory = []

    # fill the current inventory with the items that the player has
    for i in range(len(inventory)):
        if inventory[i]:
            currentInventory.append(fullInventory[i])
            

    if len(currentInventory) == 0:
        return "Empty"
    
    return currentInventory


def typeWriterEffect(msg, interval=0.01):
    """
    Print the message to the console with type writer effect. 
    Guohua.S
    """

    for i in msg:
        time.sleep(interval)
        print(i, end="")
    print()

def resetGame():
    """
    Reset the game
    """
    global hp
    global inventory
    global figure

    hp = 20
    inventory = [False, False, False]
    figure = None