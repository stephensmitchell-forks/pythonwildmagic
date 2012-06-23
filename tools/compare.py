#!/usr/bin/env python

"""Analyze Python coverage of C++."""

# Python imports.
import sys

# Application imports.
import tools
import wm5

try:
    in_file = sys.argv[1]
except:
    print 'Usage: %s in_file'%(sys.argv[0],)
    sys.exit(1)

# Read the input file of C++ names.
fin = open(in_file)
lines = fin.readlines()
fin.close()

# Assemble a lookup table of C++ names.
cpp_names = {}
for name in lines:
    name = name.strip()

    py_equiv = name

    # Trim off the leading 'Wm5::' namespace designation.
    NSPACE = 'Wm5::'
    if py_equiv[:len(NSPACE)] == NSPACE:
        py_equiv = py_equiv[len(NSPACE):]

    # Change the trailing '<float>' to 'f'.
    FTEMPL = '<float>'
    if py_equiv[len(py_equiv)-len(FTEMPL):] == FTEMPL:
        py_equiv = py_equiv[:len(py_equiv)-len(FTEMPL)] + 'f'

    # Change the trailing '<double>' to 'd'.
    DTEMPL = '<double>'
    if py_equiv[len(py_equiv)-len(DTEMPL):] == DTEMPL:
        py_equiv = py_equiv[:len(py_equiv)-len(DTEMPL)] + 'd'

    cpp_names[py_equiv] = name

# Assemble a lookup table of Python names.
py_names = {}
for name in sorted(dir(wm5)):
    py_names[name] = None

cpp_in_py = {}
for name in cpp_names.keys():
    if name in py_names:
        cpp_in_py[name] = None

py_in_cpp = {}
for name in py_names.keys():
    if name in cpp_names:
        py_in_cpp[name] = None

print 'C++ names     : %9d'%(len(cpp_names),)
print 'Python names  : %9d'%(len(py_names) ,)
print 'C++ in Python : %9d'%(len(cpp_in_py),)
print 'Python in C++ : %9d'%(len(py_in_cpp),)

num_cpp_in_py = len(cpp_in_py)
num_cpp_names = len(cpp_names)
percent = float(num_cpp_in_py) / num_cpp_names * 100
ratio_str = '%d/%d'%(num_cpp_in_py, num_cpp_names)
print 'Coverage      : %9s (%.2f%%)'%(ratio_str, percent)

for name in sorted(cpp_in_py):
    #print cpp_names[name]
    pass

# The end.