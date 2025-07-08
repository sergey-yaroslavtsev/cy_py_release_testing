from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension("my_cy.hello",
            ["src/my_cy/hello.pyx"],
                    include_dirs=[numpy.get_include()])
]

setup(
    name="cy_py_test",
    version="0.2.6",
    author="Void",
    description="A minimal Cython + Python project for testing",
    ext_modules=cythonize(extensions),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=False,
)