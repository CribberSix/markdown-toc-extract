+++
title = "Style Guide: Python (NEW)"
description = ""
menu = "main"
weight = 1
+++

-----

Authors:
[Victor Seifert](https://confluence.alexanderthamm.com/display/~victor.seifert)
[Florian Wasserrab](https://confluence.alexanderthamm.com/display/~florian.wasserrab)



https://xkcd.com/1513/

> Inexperience is a valid excuse for inefficient code, but not for the style in which it is written!



# Introduction and disclaimer

The general idea of this chapter is to give you a quick overview of the best-practice style concepts. Most of it is a shortened version of pep8, pep257, pep484 and the Google Python Style Guide. 

We won't touch every subject that is out there (e.g. source file encoding), but focus on the main points which help you and your colleagues to maintain easily readable, understandable and well documented code.

We won't delve deep into the individual concepts and edge-cases but want to offer a quick and easy way to understand the main concepts which should be followed when writing code in Python. 

For further reading, consult the links in the text or the last subsection for more in-depth materials. 


# Indentation

Use 4 **spaces** per indentation level. The exception are continuation lines where the 4 spaces indentation is optional.

Python 3 disallows mixing the use of tabs and spaces for indentation. You can configure your editor to replace tabs with spaces while typing.

# Maximum Line Length

The Python standard library is conservative and requires limiting lines to 79 characters (and docstrings/comments to 72). In general it is hard to argue a specific number for a maximum line length in the age of widescreen monitors.

One advantage of adhering to 79-ish characters per line is the possibility to have separate windows open on a single screen or to "split" your IDE between two files which remain fully readable if the code adheres to the 79-character limit per line.  

This should be understood as more of a "soft" rule, as it can make sense to break the rule in certain cases. 


# Blank Lines

Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

A file should always end in a blank line. 

Otherwhise use blank lines in code to group your code into logical blocks.

# Imports 

Imports from different packages need to be on separate lines.

Imports should be grouped in the following order with empty lines separating the groups:

1. standard library imports
2. related third party imports
3. local application/library specific imports

Wildcard imports (`from module import *`) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools.


# White spaces

White spaces can make code more readable if applied consistently.

White spaces are per definition used to separate characters, but their use does not always make things easier to read or understand if applied unnecessarily or if they are applied to logically connected characters which could potentially be split by whitespaces, but really shouldn't. 

However, you should always surround binary operators (i.e. `=, +=, -=, ==, <, >, !=, <>, <=, >=, in, not in, is, is not, and, or, not, etc.`) with a single space on either side.

Example: Immediately inside parentheses, brackets or braces:

Yes:
```python
spam(ham[1], {eggs: 2})
something_else[1:3]
```
No:
```pyton
spam( ham[ 1 ], { eggs: 2 } )
something_else[ 1 :3]
```

Example: Immediately before a comma, semicolon, or colon:

Yes:
```python
if x == 4: print x, y; x, y = y, x
```

No:
```python
if x == 4 : print x , y ; x , y = y , x
```

Avoid trailing whitespace anywhere. Since they are usually invisible, it can be confusing. 


# Comments

Code comments document the why, not the how. A comment should not express what the code is doing because the reader can see the code itself, instead it should explain the intention.

Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!

You should use two spaces after a sentence-ending period. Comments should always be complete sentences, with proper capitalization and full stops at the end.


Right hanging comments are discouraged, in favor of preceding comments.

E.g. bad:

```python
foo = blarzigop(bar) # if you don't blarzigop it, it'll shlorp.
```

Good:

```python
# If you don't blarzigop it, it'll shlorp.
foo = blarzigop(bar)
```


Use comments whereever necessary, not whereever possible. 

Don’t do this:

```python
# Increment x
x = x + 1                 
```
But sometimes, this is useful:
```python
# Compensate for border
x = x + 1                 
```

We are an international company, if you document your code in anything other than english, **we will haunt your dreams**. 

More information about documentation can be found [here]({{< relref "code_guidelines/document" >}}).

# Naming Conventions

Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.

In addition, the following special forms using leading or trailing underscores are recognized (these can generally be combined with any case convention):

- _single_leading_underscore: weak “internal use” indicator. E.g. `from M import *` does not import objects whose name starts with an underscore

- single_trailing_underscore_: used by convention to avoid conflicts with Python keyword, e.g.:   `Tkinter.Toplevel(master, class_='ClassName')`

**In General** we want to adhere to the the rule of `lower_case_with_underscores`, but as always, there are exceptions: 

- **Variable names** should be `lower_case_with_underscores`.
- **Function and method names** should be `lower_case_with_underscores`, use underscores to improve readability.
- **Class** names should normally use the `CapWords` convention.
- **Modules** should have short, `alllowercase` names, but underscores can be used in the module name if it improves readability.
- **Constants** are usually defined on a module level and written in `ALL_CAPITAL` letters with underscores separating words. 


# DocStrings 

## In General

A function must have a docstring, unless it meets all of the following criteria:

- not externally visible
- very short
- obvious

For consistency, always use `"""triple double quotes"""` around docstrings.

Use `r"""raw triple double quotes"""` if you use any backslashes in your docstrings.

Use `u"""unicode triple-quoted strings"""` if you use unicode characters in your docstrings.

## One-line docstrings

For one-line docstrings there really is only one rule: The one-line docstring should **NOT** be a string re-iterating the function/method parameters (which can be obtained by introspection).


## Multi-line docstrings

Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description. 


## Script docstrings

The docstring of a script should be usable as its *usage* message, printed when the script is invoked with incorrect or missing arguments (or perhaps with a `-h` option, for `help`). 
Such a docstring should document the script's 
- function 
- command line syntax
- environment variables
-  files. 

Usage messages can be fairly elaborate (several screens full) and should be sufficient for a new user to use the command properly, as well as a complete quick reference to all options and arguments for the sophisticated user.

## DocString format: Google DocString

You can find the official documentation [here](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings).

While there are many other docString formats out there, we have chosen Google DocString format as it is the most easily readable and one of the best structured ones. 

A further advantage of the Google format is, that the doc-strings can be parsed by `sphinx` to automatically create documentation pages.

```python
def setType(self, new_type):
    """Change the pokemon type.

        The parameter value is stored in the type
        variable of the pokemon class.

        Args:
              new_type (string): pokemon type
        Returns:
            no value
		Raises: 
               ValueError: if the string parameter is empty or consists solely of spaces
    """

	if type.strip() == "": 
        raise ValueError("No valid type was given.")

    self.type = type
    return
```

### Functions

`Args`: List each parameter by name. A description should follow the name, and be separated by a colon followed by either a space or newline. The description should include required type(s). If a function accepts *foo (variable length argument lists) and/or **bar (arbitrary keyword arguments), they should be listed as *foo and **bar.

`Returns`: (or `Yields`: for generators) Describe the type and semantics of the return value. If the function only returns None, this section is not required. 

`Raises`: List all exceptions that are relevant to the interface followed by a description. You should not document exceptions that get raised if the API specified in the docstring is violated (because this would paradoxically make behavior under violation of the API part of the API).


### Classes

Classes should have a docstring below the class definition describing the class. If your class has public attributes, they should be documented here in an Attributes section and follow the same formatting as a function’s Args section.


# Linter 

## Pylint
It helps in detecting duplicate code . It also helps in maintaining coding standards . Coding standard involves naming convention . If we go deeper it helps in finding hole in the code implementation as well . For example the interface is properly implemented or not and all dependent modules are imported or not etc . This helps coder / programmer top identify basic code health check while development .

pylint is a tool for finding bugs and style problems in Python source code. It finds problems that are typically caught by a compiler for less dynamic languages like C and C++. Because of the dynamic nature of Python, some warnings may be incorrect; however, spurious warnings should be fairly infrequent.

Pypi: https://pypi.org/project/pylint/


## black
Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

Black is a PEP 8 compliant opinionated formatter with its own style.

Black reformats entire files in place. It doesn't take previous formatting into account.

Black is able to read project-specific default values for its command line options from a pyproject.toml file. This is especially useful for specifying custom --include and --exclude/--force-exclude/--extend-exclude patterns for your project

As an example, black is used by pandas for code style tests. 

Full documentation: https://black.readthedocs.io/en/stable/index.html

Code Style with black: https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#code-style

Pypi: https://pypi.org/project/black/

## flake8
Quite similar to the above one . Basically it covers most the feature available in the above tool . I will suggest you to go through it . Because covering all the feature in very few lines , will be big injustice .

## autopep8
This utility works as python linter . It auto converts python code into pep8 standard . Basically by saying it converts into pep 8 , I mean it format the code in pep 8 standard .

## PyChecker
It is a different kind of Python linters . It basically helps in identifying hidden bugs .

## Pylama
https://pylama.readthedocs.io/en/latest/

## Bandit
It is really useful for identifying security concerns in the code. 
https://github.com/PyCQA/bandit



# A few thoughts on style-guides in general

## PEP-8: 

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important. However, know when to be inconsistent—sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment. Look at other examples and decide what looks and works best. 


## Knuth in 'Literate Programming' 
> Let us change our traditional attitude to the construction of programs: Instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do.
> The practitioner of literate programming can be regarded as an essayist, whose main concern is with exposition and excellence of style. Such an author, with thesaurus in hand, chooses the names of variables carefully and explains what each variable means. He or she strives for a program that is comprehensible because its concepts have been introduced in an order that is best for human understanding, using a mixture of formal and informal methods that reinforce each other.


# Reading list

Literate Programming, Donald E. Knuth: http://www.literateprogramming.com/knuthweb.pdf

More on writing good code & documentation:  https://www.codingthewheel.com/archives/programming-aphorisms-of-strunk-and-white/



PEP 8 – The official style guide for Python code: https://pep8.org/

PEP 257 – DocString Conventions: https://www.python.org/dev/peps/pep-0257/

PEP 526 – Syntax for Variable Annotations: https://www.python.org/dev/peps/pep-0526/

Google Python Style Guide: https://google.github.io/styleguide/pyguide.html



