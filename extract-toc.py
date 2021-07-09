import regex as re

def format_header(header): 

	# detect header level
	level = 0 
	while header[0] == '#':
		level += 1
		header = header[1:]

	# create link by replacing whitespaces with hyphens and removing colons 
	link = '#' + header.strip().replace(' ', '-').replace(':', '')
	return (header.strip(), level, link) 


# set file from which to extract a TOC 
file = "test-md.md"
with open(file, "r", encoding="utf-8") as f:
	content = f.read()

# find header lines
pattern = r"\n(#+\ .*)\n"
headers = re.findall(pattern, content)  # yields a list of strings 

# Determine header levels and format links
toc_levels = [format_header(h) for h in headers]

# Create table of contentes
toc = ['# Table of Contents']
nums = dict.fromkeys(range(1, 11), 1)
prev_level = 1
for i, (h, level, link) in enumerate(toc_levels): 

	# reset lower header-levels if current header level is higher than prev
	if prev_level > level: 
		for x in range(level+1, prev_level+1):
			nums[x] = 1

	# construct TOC element
	toc.append('\t' * (level -1 ) + f'{nums[level]}. [' + h + f']({link})' )

	# increment header level
	nums[level] = nums[level] + 1
	prev_level = level

# print toc
for _ in toc:
	print(_)