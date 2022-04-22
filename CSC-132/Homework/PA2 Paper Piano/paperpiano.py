########################################################################################
# Name: Daniel Taylor
# Date: 4/22/22
# Desc: Paper Piano
########################################################################################

from time import sleep
import pygame
from array import array

# admin stuff
USING_CIRCUITRY = False

if USING_CIRCUITRY:
    import RPi.GPIO as GPIO
else:
    GPIO = '' # stub out the errors

# constants
MIXER_FREQ = 44100 # 44.1 kHz
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

# pygame setup
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

# note class
class Note(pygame.mixer.Sound):

    def __init__(self, frequency, volume):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, buffer=self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        # calculate the period of the note's wave
        

        # calculate the amplitude


        #setup samples array


        # generate the samples

# piano class

# main program