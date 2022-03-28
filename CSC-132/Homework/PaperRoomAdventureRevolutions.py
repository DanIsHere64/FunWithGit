# Name: Daniel Taylor
# Date: 3/25/22
# Desc: Room Adventure Revolutions

from tkinter import *

# Constants
WIDTH = 800
HEIGHT = 600


# Classes
class Room:

    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    # getters/setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # additional methods
    def add_exit(self, exit, room):
        self._exits[exit] = room

    def add_item(self, item, desc):
        self._items[item] = desc

    def add_grabbable(self, item):
        self._grabbables.append(item)

    def del_grabbable(self, item):
        self._grabbables.remove(item)

    def __str__(self):
        result = f"You are in {self.name}\n"
        result += "You see:"
        for item in self.items.keys():
            result += item + " "
        result += "\n"

        result += "Exits: "
        for exit in self.exits.keys():
            result += exit + " "
        result += "\n"


class Game(Frame):

    EXIT_ACTIONS = ["quit", "exit", "bye", "adios"]
    STATUS_DEFAULT = "I don't understand. Try a noun. Valid verbs are go, look, and take."
    STATUS_DEAD = "You are dead."
    STATUS_BAD_EXIT = "Invalid exit."
    STATUS_ROOM_CHANGE = "Room changed."
    STATUS_GRABBED = "Item grabbed."
    STATUS_BAD_GRABBABLE = "I can't grab that."
    STATUS_BAD_ITEM = "I don't see that."

    def __init__(self, parent):
        self.inventory = []
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)

    def create_rooms(self):
        # create the rooms
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")

        # handle the exits
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)

        r2.add_exit("west", r1)
        r2.add_exit("south", r4)

        r3.add_exit("east", r4)
        r3.add_exit("north", r1)

        r4.add_exit("north", r2)
        r4.add_exit("west", r3)
        r4.add_exit("south", None)

        # handle the items
        r1.add_item("chair", "It is made of wicker and no one is sitting on it.")
        r1.add_item("bigger_chair", "It is made of even more wicker and no one is sitting on it. But, there is a key on it!")

        r2.add_item("fireplace", "It is made of fire and fire is sitting on it. Grab some fire and bring it with you.")
        r2.add_item("chairs", "They are made of more wicker and no one is sitting on any of them. This might be a fire hazard... Is this a chair factory?")

        r3.add_item("desk", "It is made of wicker and no one is sitting on it.")
        r3.add_item("chair", "Yep, another.")
        r3.add_item("dimmsdale_dimmadome", "Owned by Doug Dimmadome, owner of the Dimmsdale Dimmadome. That's right!")

        r4.add_item("croissant", "It is made of butter and no one is sitting on it. There is an extra stick of butter sitting next to it.")

        # handle grabbables
        r1.add_grabbable("key")
        r2.add_grabbable("fire")
        r3.add_grabbable("Doug")
        r4.add_grabbable("butter")

        # set the current room
        self.current_room = r1

    def setup_gui(self):
        # input element
        self.player_input = Entry(self, bg="WHITE")
        self.player_input.bind("<Return>", self.process)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        # the image element
        img = None
        self.image_container = Label(self, width=WIDTH // 2, image=img)
        self.image_container.image = img
        self.image_container.pack(side=LEFT, fill=Y)
        self.image_container.pack_propagate(False) # prevents image from changing window size

        # the text/status element
        text_container = Frame(self, width=WIDTH // 2)
        self.text = Text(text_container, bg="lightgrey", state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_container.pack(side=RIGHT, fill=Y)
        text_container.pack_propagate(False)

    def set_room_image(self):
        if self.current_room == None:
            img = PhotoImage(file="Skull.gif")
        else:
            img = PhotoImage(file=self.current_room.image)

        self.image_container.config(image=img)
        self.image_container.image = img

    def set_status(self, status):
        pass

    def play(self):
        self.create_rooms()
        self.setup_gui()
        self.set_room_image()
        self.set_status("")

    def process(self, event):
        pass

# Main Part

window = Tk()
window.title("Room Adventure Revolutions")
game = Game(window)
game.play()
window.mainloop()
