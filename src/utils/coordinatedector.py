# -*- coding:utf-8 -*-
#!/usr/bin/env python3


'''
this script as tool to detect the coordinate of the mouse which clicked.
features:
1. when the mouse move to one postion and click down, then the coordinates will record down.
'''

from pynput import mouse


def on_move(x, y):
    pass
    #print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    if button == mouse.Button.right:
        print('right mouse clicked, will exit the tools')
        exit(-1)
    if pressed:
        print('click the position: (' + str(x) + ',' + str(y) + ')')


def on_scroll(x, y, dx, dy):
    pass
    #print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))


    # Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:

    listener.join()
