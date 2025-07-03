from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("mymodule.hello", ["mymodule/hello.pyx"])
]

setup(
    name="my-cython-test-project",
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="A minimal Cython + Python project for testing",
    ext_modules=cythonize(extensions),
    packages=["mymodule"],
    zip_safe=False,
)