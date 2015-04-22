#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ATOM    561  O3'   C    27
"""
import sys
import os
import argparse

try:
    from diffpdb_conf import DIFF_TOOL
except ImportError:
    DIFF_TOOL = 'kompare'#'diff'


def do_file_atom_res(fn):
    """Take a file path, open the file, for each line take 
    first 31 characters, saves these lines to a new file."""

    text_new = ''
    for l in open(fn):
        if l.startswith('ATOM') or l.startswith('HETATM'):
            text_new +=  l[12:20].strip() + '\n'
    open(fn + '.out', 'w').write(text_new)

def do_file(fn):
    """Take a file path, open the file, for each line take 
    first 31 characters, saves these lines to a new file."""

    text_new = ''
    for l in open(fn):
        if l.startswith('ATOM') or l.startswith('HETATM'):
            l = l[:31].strip()
            print l
            text_new += l + '\n'
    open(fn + '.out', 'w').write(text_new)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('diffpdb.py')
    parser.add_argument('--names', help='take only atom residues names', action='store_true')
    parser.add_argument('f1', help='file')     
    parser.add_argument('f2', help='file')     

    args = parser.parse_args()
    
    str1_fn = args.f1
    str2_fn = args.f2

    if args.names:
        do_file_atom_res(str1_fn)
        do_file_atom_res(str2_fn)
    else:
        do_file(str1_fn)
        do_file(str2_fn)

    os.system(' '.join([DIFF_TOOL, str1_fn + '.out', str2_fn + '.out']))
