#!/usr/bin/env python3
from logger import logging
import uuid

class unitObject:
    def __init__(self, name, faction, image, height=1, speed=1):
        self.instanceID = uuid.uuid4().hex
        self.name = name
        self.faction = faction
        self.image = image
        self.speed = speed
        self.state = 'alive'
        self.pos = image.get_rect().move(0, height)


        self.rect = image.get_rect()
        self.radius = 8
        self.centerx = 4




    def move(self, direction):
        if direction == 'N':
            self.pos = self.pos.move(0, -self.speed)
        elif direction == 'S':
            self.pos = self.pos.move(0, self.speed)
        elif direction == 'E':
            self.pos = self.pos.move(self.speed, 0)
        elif direction == 'W':
            self.pos = self.pos.move(-self.speed, 0)
    def destroy(self):
        self.state = 'dead'   
        logging.info('Unit %s dead', self.instanceID)

class backgroundObject:
    def __init__(self, image):
        self.image = image