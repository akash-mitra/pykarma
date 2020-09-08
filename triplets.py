# Given a set of numbers find out all the
# numbers that are pythagorean triplets

from itertools import combinations

inp = input('Enter the numbers separated by space: ')

lst = list(map(lambda n: int(n), inp.split()))

for p in combinations(lst, 3):
    #
    # in a pythagorean triplet (a, b, c), satisfying the
    # equation a^2 + b^2 = c^2, following patterns are seen
    # (1) c > a and c > b,
    # (2) a + b  > c
    #
    triplet = sorted(p)
    a = triplet[0]
    b = triplet[1]
    c = triplet[2]

    if a + b > c:
        if a*a + b*b == c*c :
            print (a, b, c)

# print(lst)