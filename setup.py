import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='extracttoc',
    packages=find_packages(),
    include_package_data=True,
    description=('A CLI package to extract and create a table of contents from markdown files.'),
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/CribberSix/markdown-toc-extract',
    version='0.1',
    python_requires=">=3.6",
    author='CribberSix',
    author_email='cribbersix@gmail.com',
    install_requires=[],    
    entry_points ={
        'console_scripts': [
            'extracttoc = extracttoc.extracttoc:main'  # command = package.file:function
        ]
    },
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development',
    ],
    keywords=[],

)
