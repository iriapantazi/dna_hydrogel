#! /usr/bin/python2.7

import os
import subprocess
import glob
import sys



import json # for printing arrays in files and loading back again
import shutil
from shutil import move
from shutil import copyfile

import math
import numpy as np
np.set_printoptions(threshold=np.nan)
from numpy import linalg as LA

import scipy

import matplotlib as mpl
import matplotlib.pyplot as plt


import random 
from   random import random


import timeit  
import time

from pyquaternion import Quaternion

import pickle as pl # 

#import argparse

import csv

import readline
readline.parse_and_bind("tab: complete")
