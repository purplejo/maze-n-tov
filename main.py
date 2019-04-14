# coding: utf-8

import pygame
import sys

from menus import MainMenu
from tools.devices import Screen

pygame.init()

flags = pygame.DOUBLEBUF | pygame.FULLSCREEN | pygame.HWSURFACE
Screen(flags=flags)

MainMenu().loop()

pygame.quit()
sys.exit(0)
