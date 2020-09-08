# Given a specific string pattern, check
# how many times the pattern appear in a
# block of text

import re

texts = """
        This is a test block of the text where we
        need to search for a specific pattern. Then
        we nedd to count how many times that specific
        pattern has appeard in this block of text.
        """

regexpattern = input('Enter search pattern: ')

match = re.search(regexpattern, texts)

if match:
    print('Pattern found')

else:
    print('Pattern not present')
