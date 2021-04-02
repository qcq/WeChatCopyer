# -*- coding:utf-8 -*-
#!/usr/bin/env python3


import os
import sys
import pytest

# sys.path.append(os.path.join(os.path.dirname(
#    os.path.realpath(__file__)), '../src'))


@pytest.fixture
def cfg():
    cfg = {'config': {'platform': 'Mac'},
           'log': {'format': None},
           'Mac': {'browser': 'Chrome',
                   'whether_running': 'pgrep',
                   'file_name': 'novel.txt',
                   'snapshot_path': '/Users/qinchuanqing/Code/workspace/WeChatCopyer/res/',
                   'browser_time': 10,
                   'screen_shot': [0, 0, 100, 100],
                   'close_capture_status_bar': [0, 0, 100, 100]},
           'Windows': {'browser': 'chrome',
                       'whether_running': 'tasklist | grep',
                       'file_name': 'novel.txt',
                       'snapshot_path':
                       'C:\\Users\\oam-tester\\Downloads',
                       'browser_time': 10,
                       'screen_shot': [0, 0, 100, 100],
                       'close_capture_status_bar': [0, 0, 100, 100]},
           'Linux': {'browser': 'Chrome',
                     'whether_running': 'pgrep',
                     'file_name': 'novel.txt'}}

    yield cfg
