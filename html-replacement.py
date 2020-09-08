html_string = r'Hello <World> Goodbye & World. 2 is < 3.'

replacements = {
    '<': r'&lt;',
    '>': r'&gt;',
    '&': r'&amp;',
}

stripped = ''
for s in html_string:
    if s in replacements:
        stripped += replacements[s]
    else:
        stripped += s

print(stripped)