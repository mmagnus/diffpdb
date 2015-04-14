#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

try:
    from diffpdb_conf import DIFF_TOOL
except ImportError:
    DIFF_TOOL = 'diff'


def do_file(fn):
    """Take a file path, open the file, for each line take 
    first 31 characters, saves these lines to a new file."""

    text_new = ''
    for l in open(fn):
        if l.startswith('ATOM') or l.startswith('HETATM'):
            text_new += l[:31].strip() + '\n'
    open(fn + '.out', 'w').write(text_new)


if __name__ == '__main__':
    try:
        str1_fn = sys.argv[1]
        str2_fn = sys.argv[2]
    except:
        print 'usage: python ' + os.path.basename(__file__) \
            + ' <f1.pdb> <f2.pdb>'
        sys.exit(1)

    do_file(str1_fn)
    do_file(str2_fn)

    os.system(' '.join([DIFF_TOOL, str1_fn + '.out', str2_fn + '.out']))
