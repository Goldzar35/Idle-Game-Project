import pygame

class Player:
    def __init__(self):
        self.scavenging = False

    def is_scavenging(self):
        return self.scavenging

    def set_scavenging(self, state):
        self.scavenging = state
        print("Scavenging state set to:", state)