
import model


def saveGame(name) -> bool:
    """
    This function is written bY Sihan Wang 
    The function input is the information to be saved, including hp, name, inventory

    Saves the current character state to ./character_info.txt
    """
    now_items = model.getCurrentInventory()
    # Open file to write information
    with open("character_info.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"HP: {model.hp}\n")
        file.write("Item:[")
        for item in now_items:
            file.write(f"{item},")
        file.write("]\n")
        model.typeWriterEffect("Game Saved")
    return True

def loadGame(name) -> int:
    """
    Loads the character state from ./character_info.txt
    """

    archive = []
    # Open file to read information
    with open("character_info.txt", "r") as file:
        archive = file.readlines()
        charName = archive[0].split(":")[1].strip()
        if charName != name:
            model.typeWriterEffect("No such character")
            return -1
        else:
            model.hp = int(archive[1].split(":")[1].strip())
            inventory = archive[2].split(":")[1].strip()[1:-1].split(",")
            # remove empty string
            inventory = list(filter(None, inventory))
            if inventory == list("Empty"):
                inventory = []
            # update model.inventory with loaded inventory
            for i in range(len(inventory)):
                model.inventory[i] = True
            
            model.typeWriterEffect("Game Loaded")
            return len(inventory)