#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "ndarray.h"
#include "isosplit6.h"
#include "isocut6.h"

int isosplit6_interface(py::array_t<int> labels_out,py::array_t<double> X)
{
    NDArray<double> Xa(X);
    NDArray<int> La(labels_out);
    bigint M=Xa.shape[0];
    bigint N=Xa.shape[1];
    isosplit6_opts opts;
    isosplit6(La.ptr,M,N,Xa.ptr,opts);
    return 0;
}

int isocut6_interface(py::array_t<double> outputs,py::array_t<double> X)
{
    NDArray<double> Xa(X);
    NDArray<double> outputsa(outputs);
    bigint N=Xa.shape[0];
    isocut6_opts opts;

    double dipscore;
    double cutpoint;
    isocut6(&dipscore, &cutpoint, N, Xa.ptr, opts);
    outputsa.ptr[0] = dipscore;
    outputsa.ptr[1] = cutpoint;
    return 0;
}

PYBIND11_MODULE(isosplit6_interface, m) {
    m.doc() = "Python interface to isosplit clustering"; // optional module docstring
    
    m.def("isosplit6_interface", &isosplit6_interface, "ISO-SPLIT 6 clustering",
          py::arg("labels_out").noconvert(),
          py::arg("X").noconvert()
    );

    m.def("isocut6_interface", &isocut6_interface, "ISO-CUT 6",
          py::arg("output").noconvert(),
          py::arg("X").noconvert()
    );
}