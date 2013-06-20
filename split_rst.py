
def is_all_equal_signs(s):
	"""
		Returns True if a string consists entirely of = signs
	"""
	for c in s:
		if c != '=':
			return False
	return True
	
def is_chapter_header(text, line_num):
	"""
		Returns True if:
		1. Current line is not longer than the next line
		2. Next line consists of entirely = characters
	"""
	return (len(text[line_num]) > 0 and 
		len(text[line_num]) <= len(text[line_num+1]) and
		is_all_equal_signs(text[line_num+1]))

def header_to_filename(header_string):
	"""
		Quick and dirty conversion of a header string to a filename.
		1. Caps are lowercased.
		2. Spaces are replaced with underscores.
		
		TODO: replace any potentially bad characters. (There's gotta
		be a Python module out there that can be used for this.)
	"""
	return header_string.lower().replace(' ', '_') + ".rst"

input = open('huge_file.rst', 'r').read().split('\n')

next_filename = ""
next_file_content = []

for line_num in range(0, len(input) - 1):
	
	if is_chapter_header(input, line_num):
		
		if next_filename:
			
			# Write out next_file_content
			output = open(next_filename, 'w')
			output.write('\n'.join(next_file_content))
			output.close()
			
			# Clear the contents for the next file
			next_file_content = []
			
		next_filename = header_to_filename(input[line_num])
		
	next_file_content.append(input[line_num])
