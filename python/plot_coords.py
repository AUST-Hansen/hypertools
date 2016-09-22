#FOR CLEANUP##################################################

#Add color options

#may want to add ability to read pandas data frames
#may want to add fancier plotting options

#FOR TESTING##################################################
	
#x=np.array([[1], [2], [3], [4]]) 
#x=np.array([[1, 11], [2, 12], [3, 13], [4, 14]])
#x=np.array([[1, 11, 21], [2, 12, 22], [3, 13, 33], [4, 14, 44]])
#x=np.array([[1, 11, 21, 31], [2, 12, 22, 32], [3, 13, 33, 43], [4, 14, 44, 54]])

##############################################################

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

def plot_coords(x, *args, **kwargs):
	"""
	inputs: TxD matrix of observations
			   T-number of coords
			   D-dimensionality of each observation
			   *Nans treated as missing observations
			type (specify the type of plot)
			   see http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.plot for available options
	outputs: 1-, 2-, or 3-dimensional representation of the data
	"""

	def is_list(x):
		if type(x[0][0])==np.ndarray:
			return True
		elif type(x[0][0])==np.int64:
			return False

def resize(k):
    sizes_1=np.zeros(len(k))

    for x in range(0, len(k)):
        sizes_1[x]=k[x].shape[1]

    C=max(sizes_1)
    #find the largest number of columns of all inputted arrays

    #k=np.empty((R,C), dtype=np.ndarray)
    #m=[k]*len(args)

    m=[]
    for idx,x in enumerate(k):			
        missing=C-x.shape[1]
        add=np.zeros((x.shape[0], missing))
        y=np.append(x, add, axis=1)

        m.append(y)

	def dispatch(x):
		#determine how many dimensions (number of columns)
		if x.shape[-1]==1:
			plot1D(x)
		elif x.shape[-1]==2:
			plot2D(x)
		elif x.shape[-1]==3:
			plot3D(x)
		elif x.shape[-1]>3:
			plot3D(reduceD(x, 3))

	def plot1D(data):
		x=np.arange(len(data))
		plot2D(np.hstack((np.transpose(x), data)))

	def plot2D(data):
		# type: (object) -> object
		#if 2d, make a scatter
		plt.plot(data[:,0], data[:,1], *args, **kwargs)

	def plot3D(data):
		#if 3d, make a 3d scatter
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot(data[:,0], data[:,1], data[:,2], *args, **kwargs)

	def reduceD(x, ndim):
		#if more than 3d, reduce to 3 (PCA), then re-run
		m = PCA(n_components=ndim, whiten=True)
		#n_components=3--> reduce to 3 dimensions
		m.fit(x)
		return m.transform(x)
	
	if is_list(x):
		
		#"column pad" all arrays (rows do not matter)

		#[2] PCA over all elements
		#[3] plot

	else:
		dispatch(x)
		plt.show()

