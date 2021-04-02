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


def scroll_mouse_up(step):
    # scroll the mouse for 1 step
    mouseController.scroll(0, step)


def scroll_mouse_down(step):
    mouseController.scroll(0, -1 * step)


def scroll_to_end(cfg):
    # after scroll the mouse a while, need to capture the picture, then ocr it
    platform = cfg['config']['platform']
    coordinates = cfg[platform]['screen_shot']
    snapshot_path = cfg[platform]['snapshot_path']
    assert(len(coordinates) == 4)
    x1, y1, x2, y2 = tuple(coordinates)

    im = pyscreenshot.grab(bbox=(x1, y1, x2, y2))  # X1,Y1,X2,Y2
    current_image = os.path.join(snapshot_path, 'current_image.png')
    previous_image = os.path.join(snapshot_path, 'previous_image.png')
    im.save(current_image)
    assert(not os.path.exists(previous_image))
    assert(os.path.exists(current_image))

    while picture_to_string(current_image) != picture_to_string(previous_image):
        after_scroll_times_will_detect_whether_scroll_to_end = 10
        while after_scroll_times_will_detect_whether_scroll_to_end:
            # simulate the human readming, how long will scroll the whell of mouse
            time.sleep(random.randint(1, 5))
            scroll_mouse_down(1)
            after_scroll_times_will_detect_whether_scroll_to_end -= 1
        # take current capture image to previous image
        shutil.move(current_image, previous_image)
        assert(os.path.exists(previous_image))
        assert(not os.path.exists(current_image))
        im = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
        im.save(current_image)
        assert(os.path.exists(previous_image))
        assert(os.path.exists(current_image))

    os.remove(current_image)
    os.remove(previous_image)
    assert(not os.path.exists(previous_image))
    assert(not os.path.exists(current_image))
    return True
