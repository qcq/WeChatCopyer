# -*- coding:utf-8 -*-
#!/usr/bin/env python3

import os
from pynput import keyboard
import pyscreenshot
from listener import mouseController, keyboardController
from utils import picture_to_string
from controller import scroll_to_end, click_close_download_status_bar, click_next_chapter
import time

timeNeedToSleep = 1


# by the help of chrome of development tools


def full_wabpage_snapshot_windows():
    # reference the link https://pypi.org/project/pynput/
    print('The current pointer position is {0}'.format(
        mouseController.position))

    __click_and_release([keyboard.Key.shift, keyboard.Key.ctrl, 'i'])

    time.sleep(timeNeedToSleep)
    print('try to tap shift + ctrl + p')

    __click_and_release([keyboard.Key.shift, keyboard.Key.ctrl, 'p'])

    # Type 'Capture full size screenshot' using the shortcut type method
    __type_in_string('Capture full size screenshot')

    __click_and_release([keyboard.Key.shift, keyboard.Key.ctrl, 'i'])

    # here need to close the footer
    # the hard part is to locate the <x, y> area of close label.


def full_wabpage_snapshot_mac():
    # reference the link https://pypi.org/project/pynput/
    print('The current pointer position is {0}'.format(
        mouseController.position))

    __click_and_release([keyboard.Key.cmd, keyboard.Key.alt, 'j'])

    time.sleep(timeNeedToSleep)
    print('try to tap shift + cmd + p')

    __click_and_release([keyboard.Key.shift, keyboard.Key.cmd, 'p'])

    # Type 'Capture full size screenshot' using the shortcut type method
    __type_in_string('Capture full size screenshot')

    __click_and_release([keyboard.Key.cmd, keyboard.Key.alt, 'j'])

    # here need to close the footer
    # the hard part is to locate the <x, y> area of close label.


def __type_in_string(type_in):
    time.sleep(timeNeedToSleep)
    keyboardController.type(type_in)
    time.sleep(timeNeedToSleep)
    keyboardController.tap(keyboard.Key.enter)
    time.sleep(timeNeedToSleep)


def __click_and_release(args):
    assert(len(args) == 3)
    with keyboardController.pressed(args[0]):
        keyboardController.press(args[1])
        keyboardController.press(args[2])

    keyboardController.release(args[0])
    keyboardController.release(args[1])
    keyboardController.release(args[2])


def full_wabpage_snapshot(cfg):
    if cfg['config']['platform'] == "Mac":
        full_wabpage_snapshot_mac()
    elif cfg['config']['platform'] == "Windows":
        full_wabpage_snapshot_windows()


def get_the_neweset_snapshot_path(cfg):
    platform = cfg['config']['platform']
    path = cfg[platform]['snapshot_path']
    list_files = os.listdir(path)
    print(list_files)
    png_files = [os.path.join(path, f)
                 for f in list_files if f.endswith((".png", ".PNG"))]
    png_files.sort(key=os.path.getmtime, reverse=True)
    assert(len(png_files) != 0)
    return png_files[0]


def capture_full_book(cfg):
    temp_image = __capture_temp_image(cfg)
    # if the
    while "下一章" not in picture_to_string(temp_image):
        os.remove(temp_image)
        full_wabpage_snapshot(cfg)
        if 'current_chapter' not in cfg.keys():
            cfg['current_chapter'] = 1
        else:
            cfg['current_chapter'] += 1
        __deal_snapshot(cfg)
        click_close_download_status_bar(cfg)
        scroll_to_end(cfg)
        click_next_chapter(cfg)
        # wait 10s to load next chapter
        time.sleep(10)
        __capture_temp_image(cfg)

    os.remove(temp_image)
    cfg.pop('current_chapter')


def __capture_temp_image(cfg):
    platform = cfg['config']['platform']
    coordinates = cfg[platform]['screen_shot']
    snapshot_path = cfg[platform]['snapshot_path']
    im = pyscreenshot.grab(bbox=tuple(coordinates))  # X1,Y1,X2,Y2
    temp_image = os.path.join(snapshot_path, 'temp_image.png')

    im.save(temp_image)
    assert(os.path.exists(temp_image))
    return temp_image


def __deal_snapshot(cfg):
    print('the reader current at chapter :', cfg['current_chapter'])
    full_webpage_path = get_the_neweset_snapshot_path(cfg)
    new_name = os.path.join(os.path.dirname(
        full_webpage_path), cfg['current_chapter'] + '.png')

    os.rename(full_webpage_path, new_name)
    # should consider move them to a new folder, which can be defined in conf files
