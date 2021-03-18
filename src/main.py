# -*- coding:utf-8 -*-
#!/usr/bin/env python3

import argparse
from yamlreader import conf_parse


def __parse_cmd():
    parser = argparse.ArgumentParser(prog='WeChat Copyer', description='download e-book from web')

    parser.add_argument('-c,' '--config', metavar="PATH", dest='config', default='./conf/default.yaml', required=False, help='config file')

    args = parser.parse_args()
    return args

# parse the conf from command line
args = __parse_cmd()

# load default conf
cfg = conf_parse(args.config)

for section in cfg:
    print(section)


# 1. should logged in, can reference https://github.com/Higurashi-kagome/pythontools

# 2. open one book which want to copy by manual

# 3. start to screen capture
