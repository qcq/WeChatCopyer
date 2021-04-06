# -*- coding:utf-8 -*-
#!/usr/bin/env python3

# demo how to screenshot of the full size web page
# this test is little complicated, need to manully open webchat read website

import pytest

from handler import get_the_neweset_snapshot_path


@pytest.mark.mac
def test_screenshot_mac(mac):
    result = get_the_neweset_snapshot_path(mac)
    print(result)
    assert(result.endswith("current_image.png"))

@pytest.mark.windows
def test_screenshot_windows(windows):
    result = get_the_neweset_snapshot_path(windows)
    print(result)
    assert(result.endswith("current_image.png"))
