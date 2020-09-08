import sys

# map
word_to_num_map = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}


# Takes a set of jumbled characters and searches the word of
# a digit in it via replacement method. If the digit is found,
# it returns the remaining characters.
def check_if_word_exists_and_return_rest (chars, word):
    for c in word:
        orig_chars = chars[:]
        chars = chars.replace(c, '', 1)
        if chars == orig_chars:
            return None
    return chars


# Find all the digits of a number inside a given characters jumble
# by searching the digits sequentially and reducing the jumble
# when a digit is found.
def jumble_to_numbers (chars):
    discovered_letters = []

    # if length of chars is less than 3, no digit can be
    # found. But, in stead of hardcoding the minimum
    # digit length, we just get it from the map.
    min_search_space_len = min(word_to_num_map.items(), key=lambda x : len(x[1]))[0]

    while (len(chars) >= min_search_space_len):
        # search numbers sequentially
        for num in word_to_num_map:
            word = word_to_num_map[num]
            # check if the letters for the chosen number is present in jumble
            remaining_chars = check_if_word_exists_and_return_rest (chars, word)
            if remaining_chars != None:
                # found!
                discovered_letters.append(str(num))
                chars = remaining_chars

    # return the result in sorted manner
    return ''.join(sorted(discovered_letters))


for line in sys.stdin:
    chars = line.strip()
    print(jumble_to_numbers(chars))

# manual tests
# print('1->', jumble_to_numbers('neo'))
# print('12->', jumble_to_numbers('wtoneo'))
# print('14->', jumble_to_numbers('neofruo'))
# print('09->', jumble_to_numbers('nnieorze'))
# print('0129->', jumble_to_numbers('nniwtoneoeorze'))
# print('0012799->', jumble_to_numbers('nniwtoeneoseonvnieorezerzen'))