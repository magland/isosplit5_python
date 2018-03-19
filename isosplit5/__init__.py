import numpy as np
import isosplit5_interface

def isosplit5(X):
	X=X.astype(np.float32,copy=False,order='F') #copies only if type changes, but note that we require fortran order, which is essential for the interface
	M=X.shape[0]
	N=X.shape[1]
	labels_out=np.zeros([N]).astype(np.int32)
	isosplit5_interface.isosplit5_interface(labels_out,X)
	return labels_out