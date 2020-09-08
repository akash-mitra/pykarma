inp = input("Enter numbers separated by space: ")
n = int(input("Enter what is the n-th element: "))

lst = inp.split()

# just converting the strings to numbers
nList = list(map(lambda n: int(n), lst))

nList.sort()

# sorted list
# print(nList)

print(nList[n-1])