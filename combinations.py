from itertools import combinations

def choose_r_items_from_list(lst, r):

    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(lst, r)))
    return list(combinations(lst, r))

# Driver Function
if __name__ == "__main__":
    items = input('Enter items separated by space:')
    lst = items.split()

    r = int(input('How many items to choose (r):'))

    for c in choose_r_items_from_list(lst, r):
        print(c)