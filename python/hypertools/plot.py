#!/usr/bin/env python

"""
Wrapper function that parses plot styling arguments and calls plotting functions

INPUTS:
-numpy array(s)
-list of numpy arrays

OUTPUTS:
-None
"""

##PACKAGES##
from __future__ import division
import sys
import warnings
import re
import itertools
import seaborn as sns
from .helpers import *
from .static import static_plot
from .animate import animated_plot

##MAIN FUNCTION##
def plot(x,*args,**kwargs):

    ##STYLING##
    if 'style' in kwargs:
        sns.set(style=kwargs['style'])
        del kwargs['style']
    else:
        sns.set(style="whitegrid")

    if 'palette' in kwargs:
        sns.set_palette(palette=kwargs['palette'], n_colors=len(x))
        del kwargs['palette']
    else:
        sns.set_palette(palette="hls", n_colors=len(x))

    if 'animate' in kwargs:
        animate=kwargs['animate']
        del kwargs['animate']
    else:
        animate=False

    # if x is not a list, make it one
    if type(x) is not list:
        x = [x]

    if animate:
        animated_plot(x,*args,**kwargs)
    else:
        static_plot(x,*args,**kwargs)
