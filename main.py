import atexit
import pygame.midi
from src.midi import print_devices, readInput
from src.obs import close_obs_connection

@atexit.register
def close_obs():
    close_obs_connection()
try:
    pygame.midi.init()
    print_devices()
    my_device  = input("Enter your MIDI Controller Index: ")
    print("Selecting your Deivce:", pygame.midi.get_device_info(int(my_device))[1].decode())
    my_input = pygame.midi.Input(int(my_device))

    readInput(my_input)

except KeyboardInterrupt:
    pass 