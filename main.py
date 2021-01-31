#-*- coding: utf-8 -*-

import os
import argparse
from PIL import Image

def _is_image(ext):
    return ext.lower().endswith((".bmp", ".png", ".jpg", ".jpeg"))

def _parse_path(path):
    path = os.path.normpath(path)
    if os.path.exists(path):
        return path
    raise argparse.ArgumentTypeError("\"%s\" is not exist" % (path,))

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=_parse_path, help="file path for scan")
    parser.add_argument("--lowest-pixels", type=int, default=1000, help="lowest pixels for scan")
    return parser.parse_args()

def main():
    args = _parse_args()
    print("-------- result --------")
    scan_file_path = args.path
    lowest_pixels = args.lowest_pixels
    for root, dirs, files in os.walk(scan_file_path, topdown=False):
        remove_list = []
        for filename in files:
            path = os.path.join(root, filename)
            if not _is_image(os.path.splitext(filename)[1]):
                s = input("remove this file(%s): [y/n](default: y)" % (path,))
                if s == "n":
                    continue
                remove_list.append(path)
            else:
                with Image.open(path) as img:
                    if img.size[0] < lowest_pixels or img.size[1] < lowest_pixels:
                        remove_list.append(path)
        for path in remove_list:
            os.remove(path)
        remove_length = len(remove_list)
        if len(files) == remove_length:
            _empty_flag = True
            for filename in dirs:
                if os.path.exists(os.path.join(root, filename)):
                    _empty_flag = False
                    break
            if _empty_flag:
                os.rmdir(root)
        print("%s %d files removed." % (root, remove_length))

if __name__ == "__main__":
    main()
