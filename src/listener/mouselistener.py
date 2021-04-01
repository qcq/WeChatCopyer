# -*- coding:utf-8 -*-
#!/usr/bin/env python3

from pynput import mouse

mouseController = mouse.Controller()


def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)


listener = mouse.Listener(
    on_scroll=on_scroll
)
