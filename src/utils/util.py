# -*- coding:utf-8 -*-
#!/usr/bin/env python3

import os

def write_to_file(contents, file_out):
    with open(file_out, 'a') as f:
        f.writelines(contents)


def parse_check_if_browser_online_command(cfg):
    platform = cfg['config']['platform']
    browser = cfg[platform]['browser']
    command = cfg[platform]['whether_running']
    return command + ' ' + browser


def execute_command(command):
    result = os.system(command)
    if result != 0:
        return False
    else :
        return True

