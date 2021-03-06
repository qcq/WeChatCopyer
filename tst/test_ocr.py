# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#!/usr/bin/env python3

import pytest
from cnocr import CnOcr
import os

from utils import ocr
# to demo how to ocr one picture


def test_ocr():
    test_file = r'res/test.png'
    assert os.path.exists(test_file)
    res = ocr.ocr(test_file)
    print("Predicted Chars:", res)
    for line in res:
        print(''.join(line))

    assert res != None
    assert len(res) == 13
