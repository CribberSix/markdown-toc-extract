# extracttoc

[![PyPi](https://img.shields.io/pypi/v/extracttoc?color=blue&style=plastic)](https://pypi.org/project/extracttoc/)
![License](https://img.shields.io/github/license/Cribbersix/markdown-toc-extract?style=plastic)
[![CodeFactor](https://www.codefactor.io/repository/github/cribbersix/markdown-toc-extract/badge?style=plastic)](https://www.codefactor.io/repository/github/cribbersix/markdown-toc-extract)
![Repository size](https://img.shields.io/github/repo-size/Cribbersix/markdown-toc-extract?style=plastic)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=plastic)](https://www.python.org/)


Extract the table of contents from a markdown file with an easy to use command line tool.

## Usage

```sh
usage: extracttoc [-h] [-s] [-l LEVEL_LIMIT] file

Extracts the table of contents from a markdown file.

positional arguments:
  file                  Provide a markdown file from which to extract the toc.

optional arguments:
  -h, --help            show this help message and exit
  -s, --save            Write the table of contents to a md file. File name will be: {input-file-name}-toc.md
  -l LEVEL_LIMIT, --levels LEVEL_LIMIT
                        Set the number of levels which will be included in the TOC.
```

## Example 

```sh
extracttoc -l 2 myfile.md
```



## Limitation

The cli tool only works with hashtag-formatted headers, not with equal-sign-formatted headers! 

```
# This header will be recognized and included in the TOC 

Some text paragraph. 



This header will not be recongized. 
=== 

Some text paragraph. 

```
