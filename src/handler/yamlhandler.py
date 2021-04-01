# -*- coding:utf-8 -*-
#!/usr/bin/env python3

import yaml


def conf_parse(path_of_config):
    with open(path_of_config, "r") as yaml_file:
        cfg = yaml.load(yaml_file)
    return cfg
