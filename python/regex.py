import re 
import string

non_overlap = re.compile(r'[0-9a-fA-F]{2}') 
pairs = [ match.group(0) 
for match in non_overlap.finditer(string.hexdigits) ] 
print pairs

overlap = re.compile(r'[0-9a-fA-F](?=([0-9a-fA-F]))') 
pairs = [ match.group(0) + match.group(1) for match in overlap.finditer(string.hexdigits) ] 
print pairs



import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*-->)", "", html) #remove comment

