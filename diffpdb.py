#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
diffpdb.py - compare PDB files line by line, v.01
   usage: python ./diffpdb.py <f1.pdb> <f2.pdb>

The method is very, very simple. 

The script takes first 31 characters of lines starting with 
'HETATM' or 'ATOM' and save these lines to a <filename>.out file.

One file is created per pdb. In the final step DIFF_TOOL is executed
 on these two output files. You get a diff output. That's it! Enjoy!

Configuration:

 * DIFF_TOOL, set up what tool would you like to use to diff files (e.g. `diff` or `kompare` etc.)

"""

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
