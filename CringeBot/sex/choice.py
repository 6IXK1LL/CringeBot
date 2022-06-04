

'''
THE RANDOM CHOICE FOR
SEND GIF IN EMBED (:sex)
'''


from sex.urls import *

from random import randint


def random_choice() -> str:
    num = randint(1,3)

    if num == 1:
        return FIRST_GIF
    elif num == 2:
        return SECOND_GIF
    elif num == 3:
        return THIRD_GIF

