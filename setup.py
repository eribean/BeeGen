from setuptools import setup, convert_path

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


print(convert_path('/performance'))
if __name__ == '__main__':
    setup(
        name="BeeGen", 
        packages=['beegen'],
        package_dir={'beegen': 'beegen'},
        version="0.2",
        license="MIT",
        description="A python package for Behavioral Genetics.",
        long_description=long_description.replace('<ins>','').replace('</ins>',''),
        long_description_content_type='text/markdown',
        author='Ryan C. Sanchez',
        author_email='rsanchez44@gatech.edu',
        keywords = ['BeeGen', 'Behavioral Genetics'],
        install_requires = ['numpy', 'scipy'],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering', 
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',            
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8'
        ]
    )
