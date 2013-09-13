# different sequence of atom
echo
echo 'test #1'
./diffpdb.py 'test_data/1/1kxkA.pdb' 'test_data/1/1kxkA_M1.pdb'
# one atom different
echo
echo 'test #2'
./diffpdb.py 'test_data/2/str1.pdb' 'test_data/2/str2.pdb'
# identical
echo
echo 'test #3'
./diffpdb.py 'test_data/3.ident/str1.pdb' 'test_data/3.ident/str2.pdb'


