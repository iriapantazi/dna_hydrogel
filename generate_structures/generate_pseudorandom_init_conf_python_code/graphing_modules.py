#! /usr/bin/python


import itertools
import pylab


from   itertools import product,imap
from   matplotlib.backends.backend_pdf import PdfPages
# from   __main__ import *
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'large',
          'figure.figsize': (11, 6),
          'axes.labelsize': 'x-large',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)
import matplotlib.cm as cm


from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.text import Annotation

from mpl_toolkits.mplot3d import Axes3D


