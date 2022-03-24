import pygame.midi

from src.obs import get_scenes, switch_connection

def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

def readInput(input_device):
    all_scenes = get_scenes()
    while True:
        if input_device.poll():
            event = input_device.read(1)
            in_key = event[0][0][1] - 36
            try:
                my_scene = all_scenes[in_key]
                switch_connection(my_scene)
            except:
                print("Key not yet registered")