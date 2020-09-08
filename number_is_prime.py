import math

n = int(input('Enter a number: '))

root = int(math.sqrt(n))

for i in range(2, root+1):
    if n % i == 0:
        print('Not prime.', n, ' is divisible by ', i)
        exit()

print('Prime Number')