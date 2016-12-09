To install, navigate to this folder in Terminal and type:

pip install -e .

(this assumes you have pip installed on your system: https://pip.pypa.io/en/stable/installing/)

<h2>Main functions</h2>

+ hyp.plot - plots static data or movie
+ hyp.align - hyperaligns multidimensional data
+ hyp.reduce - implements PCA to reduce dimensionality of data
+ hyp.describe - plots/analyses to evaluate how well the functions above are working

<h2>hyp.plot</h2>

Inputs:

X: a T by D matrix of observations.  T is the number of coordinates
and D is the dimensionality of each observation.  NaNs are
treated as missing observations.

Arguments:

Format strings can be passed as a string, or tuple/list of length x.
See matplotlib API for more styling options

Keyword arguments:

palette (string): A matplotlib or seaborn color palette

color (list): A list of colors for each line to be plotted. Can be named colors, RGB values (e.g. (.3, .4, .1)) or hex codes. If defined, overrides palette. See http://matplotlib.org/examples/color/named_colors.html for list of named colors. Note: must be the same length as X.

point_colors (list of str, floats or ints): A list of colors for each point. Must be dimensionality of data (X). If the data type is numerical, the values will be mapped to rgb values in the specified palette.  If the data type is strings, the points will be labeled categorically.

linestyle (list): a list of line styles

marker (list): a list of marker types

See matplotlib API for more styling options

labels (list): A list of labels for each point. Must be dimensionality of data (X). If no label is wanted for a particular point, input `None`

explore (bool): (experimental feature) Displays user defined labels or PCA coordinates on hover. When a point is clicked, the label will remain on the plot (WIP). To use, set `explore=True`.

<h2>Example uses</h2>

Import the library: `import hypertools as hyp`

Plot with default color palette: `hyp.plot(w)`

Plot as movie: `hyp.plot(w, animate=True)`

Change color palette: `hyp.plot(w,palette='Reds')`

Specify colors using unlabeled list of format strings: `hyp.plot([w[0],w[1]],['r:','b--'])`

Plot data as points: `hyp.plot([w[0],w[1]],'o')`

Specify colors using keyword list of colors (color codes, rgb values, hex codes or a mix): `hyp.plot([w[0],w[1],[w[2]],color=['r', (.5,.2,.9), '#101010'])`

Specify linestyles using keyword list: `hyp.plot([w[0],w[1],[w[2]],linestyle=[':','--','-'])`

Specify markers using keyword list: `hyp.plot([w[0],w[1],[w[2]],marker=['o','*','^'])`

Specify markers with format string and colors with keyword argument: `hyp.plot([w[0],w[1],[w[2]], 'o', color=['r','g','b'])``

Specify labels:
```
# Label first point of each list
labels=[]
for idx,i in enumerate(w):
    tmp=[]
    for iidx,ii in enumerate(i):
        if iidx==0:
            tmp.append('Point ' + str(idx))
        else:
            tmp.append(None)
    labels.append(tmp)

hyp.plot(w, 'o', labels=labels)
```

Specify point_colors:
```
# Label first point of each list
point_colors=[]
for idx,i in enumerate(w):
    tmp=[]
    for iidx,ii in enumerate(i):
            tmp.append(np.random.rand())
    point_colors.append(tmp)

hyp.plot(w, 'o', point_colors=point_colors)
```

Turn on explore mode (experimental): `hyp.plot(w, 'o', explore=True)`
