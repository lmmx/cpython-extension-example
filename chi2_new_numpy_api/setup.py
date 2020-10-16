from distutils.core import setup, Extension
import numpy.distutils.misc_util

setup(
    ext_modules=[
        Extension(
            "_chi2", ["_chi2.c", "chi2.c"],
            define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]
        )
    ],
    include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
)
