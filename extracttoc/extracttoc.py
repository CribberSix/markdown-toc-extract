import sys
from os.path import exists
import regex as re
import argparse
import pyperclip as cp

from typing import List, Tuple

def format_header(header: str) -> Tuple[str, int, str]:
    """Calculates the level of the header, removes leading and trailing whitespaces and creates the markdown-link.

    :param header: header line from the markdown file
    :return: a tuple consisting of the cleaned header, the header level and the formatted markdown link.
    """

    # determine header level
    level = 0
    while header[0] == "#":
        level += 1
        header = header[1:]

    # create clickable link by replacing whitespaces with hyphens and removing colons
    headerlink = "#" + re.sub(r'[^a-zA-Z 0-9]', '', header).lower().strip().replace(" ", "-").replace("--", "-")
    return (header.strip(), level, headerlink)


def remove_code_blocks(content: List[str]) -> List[str]:
    """Removes lines starting with "```" (=code blocks) from the markdown file.

    Since code blocks can contain lines with leading hashtags
    (e.g. comments in python) they need to be removed before looking for headers.

    :param content: file contents as a list of strings
    :return: Cleaned List without codeblock lines
    :rtype: List<str>
    """
    content_cleaned = []
    code_block = False

    for x in content:
        if x[:3] == '```':
            code_block = not code_block
        elif not code_block:
            content_cleaned.append(x)

    return content_cleaned


def create_toc(toc_levels: List[Tuple[str, int, str]], level_limit: int) -> List[str]:
    """Creates a list of strings representing the items in the table of content.

    The function works up to 111 header levels.

    :param toc_levels:  A list containing a tuple consisting of the header,
    					the level of the header and a formatted markdown-link to the header.
    :param level_limit: Limits the number of levels included in the TOC
    :return: Ordered items of the table of contents.

    Example for toc_levels:

            [
                    ('First Header', 1, '#First-Header')
                    ('Second level', 2, '#Second-level')
                    ('First level again', 1, '#First-level-again')
            ]
    """

    toc = ["# Table of Contents"]
    # create a dict to store the header numbering for each level
    max_level = max([x[1] for x in toc_levels]) + 1
    nums = dict.fromkeys(range(1, max_level), 1)
    prev_level = 1
    for i, (h, level, link) in enumerate(toc_levels):

        # reset lower header-levels if current header level is higher than prev
        if prev_level > level:
            for x in range(level + 1, prev_level + 1):
                nums[x] = 1

        # construct TOC element
        if level <= level_limit:
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
        help="Write the TOC to a md file. File name will be: {input-file-name}-toc.md",
    )

    parser.add_argument(
        "-c",
        "--copy",
        action="store_true",
        dest="save_to_clipboard",
        help="Copy the TOC to your clipboard",
    )

    parser.add_argument(
        "-i",
        "--insert",
        action="store_true",
        dest="insert_in_file",
        help="Insert the TOC directly into the file in front of the first line.",
    )

    parser.add_argument(
        "-l",
        "--levels",
        dest="limit",
        default=3,
        type=int,
        help="Set the number of levels which will be included in the TOC.",
    )

    args = parser.parse_args()

    # read file
    file = args.file[0]

    if not exists(file):
        raise ValueError(f"File {file} could not be found.")

    with open(file, "r", encoding="utf-8") as f:
        content = f.read().split("\n")

    # remove code-blocks by iterating over lines and skipping lines between lines which start with ``` ....
    content_cleaned = remove_code_blocks(content) 

    # identify header lines of both types
    headers = []
    re_hashtag_headers = r"^#+\ .*$"
    re_alternative_header_lvl1 = r"^=+ *$"
    re_alternative_header_lvl2 = r"^-+ *$"

    for i, line in enumerate(content_cleaned): 
        # identify headers by leading hashtags
        if re.search(re_hashtag_headers, line): 
            headers.append(line)
        # identify alternative headers
        elif re.search(re_alternative_header_lvl1, line): 
            # add previous header line with unified format
            headers.append('# ' + content_cleaned[i-1])  
        elif re.search(re_alternative_header_lvl2, line): 
            # add previous header line with unified format
            headers.append('## ' + content_cleaned[i-1]) 

    # determine header levels and format links
    toc_levels = [format_header(h) for h in headers]

    # Create table of contents
    toc = create_toc(toc_levels, args.limit)

    # Output toc
    for _ in toc:
        print(_)

    if args.save_to_clipboard:
        cp.copy("\n".join(toc))

    if args.insert_in_file:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        new = "\n".join(toc) + "\n\n" + content

        with open(file, "w", encoding="utf-8") as f:
            f.write(new)

    if args.save_to_md:
        print(f"\n\nWriting TOC to {file}-toc.md ...")

        # determine filename
        if file[-3:] == '.md':
            output_name = file[:-3] + '-toc.md'
        elif file[-9:] == '.markdown':
            output_name = file[:-9] + '-toc.markdown'
        else:
            output_name = file + '-toc.md'

        with open(output_name, "w") as writer:
            for f in toc:
                writer.write(f + "\n")
