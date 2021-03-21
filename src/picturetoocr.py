# -*- coding:utf-8 -*-
#!/usr/bin/env python3

from cnocr import CnOcr
import os

ocr = CnOcr()


def picture_to_string(path):
    if not os.path.exists(path):
        print(path, "non-exist")
        return
    res = ocr.ocr(path)
    result = [''.join(line) for line in res]
    return result
