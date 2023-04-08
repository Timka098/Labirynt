import pygame
import os
# создаєм клас звуків
class Sound:
    def __init__(self, path, volume=1):
        # повний путь до папки звуків
        self.ABSOLUTE_PATH = os.path.join(os.path.abspath(__file__ +'/..'), path)
        # создаєм звук по повнуму шляху
        self.SOUND = pygame.mixer.Sound(self.ABSOLUTE_PATH)
        # уснановлюєм громкость звуку
        self.SOUND.set_volume(volume)
    def play(self, start=0):
        # метод для проігрування звуку
        self.SOUND.play(0, start, 0)
