#!/usr/bin/env python3

class unitObject:
    def __init__(self, instanceID, name, faction, image, height, speed, state):
        self.instanceID = instanceID
        self.name = name
        self.faction = faction
        self.speed = speed
        self.image = image
        self.state = state
        self.pos = image.get_rect().move(0, height)
    def move(self, direction):
        if direction == 'N':
            self.pos = self.pos.move(0, -self.speed)
        elif direction == 'S':
            self.pos = self.pos.move(0, self.speed)
        elif direction == 'E':
            self.pos = self.pos.move(self.speed, 0)
        elif direction == 'W':
            self.pos = self.pos.move(-self.speed, 0)

class backgroundObject:
    def __init__(self, image):
        self.image = image