# -*- coding: utf-8 -*-
"""
=============================
Precognition
=============================

The future trajectory of an animated plot can be visualized with the precog
argument.  This displays a low opacity version of the trace ahead of the
current points being plotted.  This can be used in conjunction with the
chemtrails argument to plot a low-opacity trace of the entire timeseries.
"""

# Code source: Andrew Heusser
# License: MIT

# import
import hypertools as hyp
import numpy as np

# load example data
data = hyp.load('weights', align='hyper')

# average into 2 groups
w1 = np.mean(data[:17],0)
w2 = np.mean(data[18:],0)

# plot
hyp.plot([w1, w2], animate=True, precog=True)
