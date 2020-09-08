import sys

line = 'reuonnoinfe'

from itertools import permutations

word_to_num_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def remove_resolved_chars(string, removals):
    for c in removals:
        string = string.replace(c, '', 1)
    return string


def find_a_digit (jumble):
    min_len = 3
    max_len = 6
    for i in range(min_len, max_len):
        for p in list(permutations(jumble, i)):
            c = ''.join(p)
            if c in word_to_num_map:
                return (word_to_num_map[c], c)
    return (None, None)


chars = line.strip()
min_len = 3
print ("original", chars)

while (True):
    if len(chars) < min_len: break

    digit, word = find_a_digit(chars)
    if word == None: break;

    print(digit, word)
    chars = remove_resolved_chars(chars, word)

    print ("remaining", chars)
