# -*- coding:utf-8 -*-
#!/usr/bin/env python3

import os
from pynput import mouse, keyboard
import time

timeNeedToSleep = 1

mouseController = mouse.Controller()
keyboardController = keyboard.Controller()

# by the help of chrome of development tools


def full_wabpage_snapshot(x, y):
    # reference the link https://pypi.org/project/pynput/
    print('The current pointer position is {0}'.format(
        mouseController.position))

    # Set pointer position
    # mouseController.position = (x, y)
    # print('Now we have moved it to {0}'.format(mouseController.position))

    # Double click; this is different from pressing and releasing
    # mouseController.click(mouse.Button.left, 1)

    # Scroll two steps down
    # mouseController.scroll(0, 2)

    with keyboardController.pressed(keyboard.Key.shift):
        keyboardController.press(keyboard.Key.ctrl)
        keyboardController.press('i')

    keyboardController.release(keyboard.Key.shift)
    keyboardController.release(keyboard.Key.ctrl)
    keyboardController.release('i')

    time.sleep(timeNeedToSleep)
    print('try to tap shift + ctrl + p')

    with keyboardController.pressed(keyboard.Key.shift):
        keyboardController.press(keyboard.Key.ctrl)
        keyboardController.press('p')

    keyboardController.release(keyboard.Key.shift)
    keyboardController.release(keyboard.Key.ctrl)
    keyboardController.release('p')

    # Type 'Capture full size screenshot' using the shortcut type method
    time.sleep(timeNeedToSleep)
    print('ready to input')
    keyboardController.type('Capture full size screenshot')

    time.sleep(timeNeedToSleep)
    print('ready to input')

    keyboardController.tap(keyboard.Key.enter)

    time.sleep(timeNeedToSleep)
    print('ready to input')

    with keyboardController.pressed(keyboard.Key.shift):
        keyboardController.press(keyboard.Key.ctrl)
        keyboardController.press('i')

    keyboardController.release(keyboard.Key.shift)
    keyboardController.release(keyboard.Key.ctrl)
    keyboardController.release('i')

    # here need to close the footer
    # the hard part is to locate the <x, y> area of close label.


def get_the_neweset_snapshot_path(path):
    list_files = os.listdir(path)
    print(list_files)
    png_files = [os.path.join(path, f)
                 for f in list_files if f.endswith(".app")]
    png_files.sort(key=os.path.getmtime, reverse=True)
    assert(len(png_files) != 0)
    return png_files[0]


def scroll_mouse(step):
    # scroll the mouse for 1 step
    mouseController.scroll(0, step)


def scroll_to_end():
    # after scroll the mouse a while, need to capture the picture, then ocr it
    previousImage = None
    currentImage = None  # take image

    while currentImage != previousImage:
        after_scroll_times_will_detect_weather_scroll_to_end = 10
        while after_scroll_times_will_detect_weather_scroll_to_end
        scroll_mouse(1)
        after_scroll_times_will_detect_weather_scroll_to_end -= 1
        previousImage = currentImage
        currentImage = None


def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)


listener = mouse.Listener(
    on_scroll=on_scroll
)
# get_the_neweset_snapshot_path('/Users/qinchuanqing/Downloads')
# time.sleep(100)
