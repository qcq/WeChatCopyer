# -*- coding:utf-8 -*-
#!/usr/bin/env python3


import shutil
import random
import time
from utils import picture_to_string
from listener import mouseController
import pyscreenshot
import os
import sys

from pynput.mouse import Button


def scroll_mouse_up(step):
    # scroll the mouse for 1 step
    mouseController.scroll(0, step)


def scroll_mouse_down(step):
    mouseController.scroll(0, -1 * step)


def scroll_to_end(cfg, times=1):
    # after scroll the mouse a while, need to capture the picture, then ocr it
    platform = cfg['config']['platform']
    coordinates = cfg[platform]['screen_shot']
    snapshot_path = cfg[platform]['snapshot_path']
    step = cfg[platform]['step'] * times
    assert(len(coordinates) == 4)

    im = pyscreenshot.grab(bbox=tuple(coordinates))  # X1,Y1,X2,Y2
    current_image = os.path.join(snapshot_path, 'current_image.png')
    previous_image = os.path.join(snapshot_path, 'previous_image.png')
    im.save(current_image)
    assert(not os.path.exists(previous_image))
    assert(os.path.exists(current_image))

    while picture_to_string(current_image) != picture_to_string(previous_image):
        after_scroll_times_will_detect_whether_scroll_to_end = 10
        # simulate the human readming, how long will scroll the whell of mouse
        time.sleep(random.randint(1, 3))
        while after_scroll_times_will_detect_whether_scroll_to_end:
            scroll_mouse_down(step)
            after_scroll_times_will_detect_whether_scroll_to_end -= 1
        # take current capture image to previous image
        shutil.move(current_image, previous_image)
        assert(os.path.exists(previous_image))
        assert(not os.path.exists(current_image))
        im = pyscreenshot.grab(bbox=tuple(coordinates))
        im.save(current_image)
        assert(os.path.exists(previous_image))
        assert(os.path.exists(current_image))

    os.remove(current_image)
    os.remove(previous_image)
    assert(not os.path.exists(previous_image))
    assert(not os.path.exists(current_image))
    return True


def click_close_download_status_bar(cfg):
    # mouse move to position <x, y>
    platform = cfg['config']['platform']
    status_bar_position = cfg[platform]['close_capture_status_bar']
    mouseController.position = tuple(status_bar_position)
    # mouse click the left button

    mouseController.press(Button.left)
    mouseController.release(Button.left)


def click_next_chapter(cfg):
    # mouse move to position <x, y>
    platform = cfg['config']['platform']
    next_chapter_position = cfg[platform]['next_chapter']
    assert(len(next_chapter_position) == 4)
    # take the coordinate to random positipn from area
    x = random.randint(next_chapter_position[0], next_chapter_position[2])
    y = random.randint(next_chapter_position[1], next_chapter_position[3])
    mouseController.position = (x, y)
    # mouse click the left button
    mouseController.press(Button.left)
    mouseController.release(Button.left)
