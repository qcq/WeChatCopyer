# -*- coding:utf-8 -*-
#!/usr/bin/env python3

def __count_file(file):
    counter = 0
    with open(file, 'r') as f_in:
        commnet_out = False
        for line in f_in:
            # skip the commnets of single line
            if line.strip().startswith('#'):
                continue
            # skip the multi-line comments
            if not commnet_out and (line.strip().startswith("'''") or line.strip().startswith('"""')):
                commnet_out = True
                continue
            if commnet_out and (line.strip().startswith("'''") or line.strip().startswith('"""')):
                commnet_out = False
                continue
            if commnet_out:
                continue
            # skip the empty line
            if line.strip() == "":
                continue
            counter = counter + 1
        return counter


if __name__ == "__main__":
    included_file_to_count = ['src/main.py', 'src/picturetoocr.py', 'src/webpagesnap.py',
                              'src/yamlreader.py', 'src/utils/util.py']

    data = {file: __count_file(file) for file in included_file_to_count}
    print(data)

    lines = sum(data.values())
    print(lines)
