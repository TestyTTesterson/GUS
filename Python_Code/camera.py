import pygame
from pygame import camera

from time import sleep

camera.init()
camlist = camera.list_cameras()

cam = camera.Camera(camlist[0], (640, 480))
if camlist:
    image = cam.get_image()
    image.save(image, "/homt/testyt/Pictures/testing123.jpg")