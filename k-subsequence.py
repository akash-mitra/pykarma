# k-subsequence
# Find all the contiguous sequence of numbers in an array
# so that the sum of a sequence is divisible by k and the
# length of the sequence is not greater than k.

k = int(input('Enter k: '))
n = int(input('No of elements in array: '))
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(i+1, n+1):
        subset = arr[i:j]
        if len(subset) <= k and sum(subset) % k == 0:
            print (subset)


# arr = [3, 5, 1, 2, 3, 4, 1]
# k = 3