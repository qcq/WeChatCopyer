# -*- coding:utf-8 -*-
#!/usr/bin/env python3

from pynput import mouse, keyboard
import time

timeNeedToSleep = 1

mouseController = mouse.Controller()
keyboardController = keyboard.Controller()

# by the help of chrome of development tools
def full_wabpage_snapshot(x, y):
    # reference the link https://pypi.org/project/pynput/
    print('The current pointer position is {0}'.format(mouseController.position))

    # Set pointer position
    mouseController.position = (x, y)
    print('Now we have moved it to {0}'.format(mouseController.position))

    # Double click; this is different from pressing and releasing
    mouseController.click(mouse.Button.left, 1)

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



def scroll_mouse(step):
    # scroll the mouse for 1 step
    mouseController.scroll(0, step)

def scroll_to_end():
    # after scroll the mouse a while, need to capture the picture, then ocr it
    previousImage = None
    currentImage = pass # take image

    while currentImage != previousImage:
        scroll_mouse(1)


def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)


listener = mouse.Listener(
    on_scroll=on_scroll
)

#time.sleep(100)


