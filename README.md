# extracttoc

[![PyPi](https://img.shields.io/pypi/v/extracttoc?color=blue&style=plastic)](https://pypi.org/project/extracttoc/)
![License](https://img.shields.io/github/license/Cribbersix/markdown-toc-extract?style=plastic)
[![CodeFactor](https://www.codefactor.io/repository/github/cribbersix/markdown-toc-extract/badge?style=plastic)](https://www.codefactor.io/repository/github/cribbersix/markdown-toc-extract)
![Repository size](https://img.shields.io/github/repo-size/Cribbersix/markdown-toc-extract?style=plastic)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=plastic)](https://www.python.org/)


Extract a table of contents from a markdown file via cmd.


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


