import numpy as np
import isosplit5_interface
import isosplit6_interface

def isosplit5(X):
	X=X.astype(np.float64,copy=False,order='F') #copies only if type changes, but note that we require fortran order, which is essential for the interface
	M=X.shape[0]
	N=X.shape[1]
	labels_out=np.zeros([N]).astype(np.int32)
	isosplit5_interface.isosplit5_interface(labels_out,X)
	return labels_out

def isocut5(X):
	X=X.astype(np.float64,copy=False,order='F') #copies only if type changes, but note that we require fortran order, which is essential for the interface
	N=X.shape[0]
	output=np.zeros((2,), dtype=np.float64)
	isosplit5_interface.isocut5_interface(output,X)
	dipscore = output[0]
	cutpoint = output[1]
	return dipscore, cutpoint

def isosplit6(X):
	X=X.astype(np.float64,copy=False,order='F') #copies only if type changes, but note that we require fortran order, which is essential for the interface
	M=X.shape[0]
	N=X.shape[1]
	labels_out=np.zeros([N]).astype(np.int32)
	isosplit6_interface.isosplit6_interface(labels_out,X)
	return labels_out

def isocut6(X):
	X=X.astype(np.float64,copy=False,order='F') #copies only if type changes, but note that we require fortran order, which is essential for the interface
	N=X.shape[0]
	output=np.zeros((2,), dtype=np.float64)
	isosplit6_interface.isocut6_interface(output,X)
	dipscore = output[0]
	cutpoint = output[1]
	return dipscore, cutpoint