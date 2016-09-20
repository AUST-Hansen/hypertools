	import numpy as np
	def align(*args):

		sizes_0=np.zeros((len(args)))
		sizes_1=np.zeros((len(args)))

		#STEP 0: STANDARDIZE SIZE AND SHAPE	
		for x in range(0, len(args)):
			sizes_0[x]=args[x].shape[0]
			T=min(sizes_0)
			#find the smallest number of rows

			sizes_1[x]=args[x].shape[1]
			T=max(sizes_1)
			#find the largest number of columns


		for x in args:
			x=x[0:T,:]
			#reduce each input argument to the minimum number of rows by deleting excess rows

			missing=T-x.shape[1]
			add=np.zeros((T, missing))
			y=np.append(x, add, axis=1)
			#add 'missing' number of columns (zeros) to each array

			#TEST
			print args