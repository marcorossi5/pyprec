#!/bin/bash
: '
Script to test pyprec package.

Creates a new package named foo, installs it through pip and checks that it runs.

Usage: (from example/folder)

$ ./example
'
# run pyprec
pyprec --runcard example_runcard.yaml
# test pyfoo package
cd foo
echo Installing pyfoo package ...
pip install -e . > /dev/null
echo Testin pyfoo package ...
echo
pyfoo
echo
echo Uninstalling pyfoo package ...
pip uninstall pyfoo -y > /dev/null
cd ..
rm -rf foo
echo Done: test completed !