from itertools import combinations

if __name__ == '__main__':
    items = input('Enter items separated by space:')
    lst = items.split()

    for p in list(combinations(lst)):
        print (p)