# -*- coding:utf-8 -*-
#!/usr/bin/env python3

# demo how to screenshot of the full size web page
# this test is little complicated, need to manully open webchat read website

import pytest

from handler import get_the_neweset_snapshot_path


def test_screenshot(cfg):
    result = get_the_neweset_snapshot_path(cfg)
    assert(result.endswith("current_image.png"))
