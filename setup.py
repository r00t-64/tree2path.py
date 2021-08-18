import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='tree2path',  
     version='0.1',
     scripts=['tree2path'] ,
     author="Isaac Alexis Rivera Sanchez",
     author_email="ariveras@uni.pe",
     description="Create path and files given a formatted link file as an input",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/r00t-64/tree2path.py",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
         "Operating System :: OS Independent",
     ],
 )