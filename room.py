from constants import room_size

class Room:
    def __init__(self):
        self.height = room_size[2]
        self.width = room_size[1]
        self.length = room_size[0]

room = Room()