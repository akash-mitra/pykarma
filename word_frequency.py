
text ="Ringa Ringa roses, pocket full of poses, yachoo yachoo we all fall down down."

words=text.split()
counter = {}

# count how many times a word is used.
for word in words:

    # just remove some of the punctuation marks
    word = word.strip(".,!?")

    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

# for sorting a dictionary, one idea is to
# convert the dictionary in a iterable tuples
# and then specifying the "sort key" based on
# which the sort should happen as a lambda function.
sorted_counter = sorted(counter.items(), key=lambda word: word[1], reverse=True)

# print the top 3 items
# print(sorted_counter[:3])

# print the sorted list
print(sorted_counter)