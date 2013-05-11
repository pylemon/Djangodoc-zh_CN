#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

cur_dir = os.path.dirname(os.path.abspath(globals()["__file__"]))
path = os.path.join(cur_dir, 'translations/zh_CN/LC_MESSAGES/')

def compile_po(po_filename):
    """ compile po files into mo files.
    """
    filename, ext = os.path.splitext(po_filename)
    input_filename = "{0}{1}".format(filename, ext)
    output_filename = "{0}.mo".format(filename)
    cmd = 'msgfmt "{2}{0}" -o "{2}{1}"'.format(input_filename, output_filename, path)
    print cmd
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

if __name__ == '__main__':
    # --- run the `$ tx pull` to fetch the online translations

    # --- run the compile_po to make mo files
    for filename in os.listdir(path):
        compile_po(filename)
