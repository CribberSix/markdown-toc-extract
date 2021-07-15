import sys
from os.path import exists
import regex as re
import argparse


def format_header(header):
    """Formatting tasks. 

    Removes leading or trailing whitespaces. 
    Calculates the level of the header. 
    Creates the markdown-link.

    :param header: Header line from the markdown file
    :type header: str
    :return: A tuple consisting of the cleaned header, the header level and the formatted markdown link. 
    :rtype: Tuple<str, str, str>
    """

    # detect header level
    level = 0
    while header[0] == "#":
        level += 1
        header = header[1:]

    # create link by replacing whitespaces with hyphens and removing colons
    link = "#" + header.strip().replace(" ", "-").replace(":", "")
    return (header.strip(), level, link)


def remove_code_blocks(content):
    """Removes code blocks from the markdown file.

    Since code blocks can contain lines with leading hashtags 
    (e.g. comments in python) they need to be removed before looking for headers.

    :param content: file contents as a list of strings
    :type content: List<str>
    :return: Cleaned List without codeblock lines
    :rtype: List<str>
    """
    pattern_codeblock = r"^```"
    content_cleaned = []
    code_block = False

    for x in content.split("\n"):
        if len(re.findall(pattern_codeblock, x)) > 0:
            code_block = not code_block
        if not code_block:
            content_cleaned.append(x)

    return content_cleaned


def create_toc(toc_levels):
    """Creates a list of strings representing the items in the table of content.


    :param toc_levels:  A list containing a tuple consisting of the header, 
    					the level of the header and a formatted markdown-link to the header.
    :type toc_levels: List<Tuple<str, int, str>>
    :return: Ordered items of the table of contents.
    :rtype: List<str>

    Example for toc_levels:

            [
                    ('First Header', 1, '#First-Header')
                    ('Second level', 2, '#Second-level')
                    ('First level again', 1, '#First-level-again')
            ]

    """

    toc = ["# Table of Contents"]
    nums = dict.fromkeys(range(1, 111), 1)
    prev_level = 1
    for i, (h, level, link) in enumerate(toc_levels):

        # reset lower header-levels if current header level is higher than prev
        if prev_level > level:
            for x in range(level + 1, prev_level + 1):
                nums[x] = 1

        # construct TOC element
        toc.append("\t" * (level - 1) + f"{nums[level]}. [" + h + f"]({link})")

        # increment header level
        nums[level] = nums[level] + 1
        prev_level = level
    return toc


def main():

    parser = argparse.ArgumentParser(
        prog="extracttoc",
        description="Extracts the table of contents from a markdown file.",
    )

    parser.add_argument(
        "file",
        nargs=1,
        help="Provide a markdown file from which to extract the toc.",
        type=str,
    )

    parser.add_argument(
        "-s",
        "--save",
        action="store_true",
        dest="save_to_md",
        help="Write the table of contents to a md file. File name will be: {input-file-name}-toc.md",
    )

    args = parser.parse_args()

    # read file
    file = args.file[0]

    if not exists(file):
        raise ValueError(f"File {file} could not be found.")

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # remove code-blocks by iterating over lines and skipping lines between lines which start with ``` ....
    content_cleaned = "\n".join(remove_code_blocks(content))

    # find header lines and determine header levels and format links
    pattern = r"\n(#+\ .*)\n"
    headers = re.findall(pattern, content_cleaned)  # yields a list of strings
    toc_levels = [format_header(h) for h in headers]

    # Create table of contents
    toc = create_toc(toc_levels)

    # Output toc
    for _ in toc:
        print(_)

    if args.save_to_md:
        print(f"\n\nWriting TOC to {file}-toc.md ...")
        with open(f"{file}-toc.md", "w") as writer:
            for f in toc:
                writer.write(f + "\n")
