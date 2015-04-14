diffpdb
-------------------------------------------------------------------------------

    diffpdb.py - compare PDB files line by line, v.01
       usage: python ./diffpdb.py <f1.pdb> <f2.pdb>

The method is very, very simple. 

The script takes first 31 characters of lines starting with 
'HETATM' or 'ATOM' and save these lines to a <filename>.out file.

One file is created per pdb. In the final step DIFF_TOOL is executed
 on these two output files. You get a diff output. That's it! Enjoy!

Configuration:

 * DIFF_TOOL, set up what tool would you like to use to diff files (e.g. `diff` or `kompare` etc.)

![screenshot](screenshot.png)
