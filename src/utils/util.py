# -*- coding:utf-8 -*-
#!/usr/bin/env python3

def write_to_file(contents, file_out):
    with open(file_out, 'a') as f:
        f.writelines(contents)
