#! /usr/bin/python2.7

import argparse

parser = argparse.ArgumentParser(description='Input for the load_plot.py')

parser.add_argument('integers', metavar='-s', type=str, nargs='+',
                    help='input coordinates file N molecules and box size')

parser.add_argument('--infile','-i', action="store")
parser.add_argument('--nmol'  ,'-n', action="store")
parser.add_argument('--box'   ,'-b', action="store")


args = parser.parse_args()
print args

#print(args.accumulate(args.integers))

