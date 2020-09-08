def isPel(string):
    l = len(string)
    i = 0
    while(i<l):
        start = string[i]
        end = string[l-1-i]
        if (start != end):
            return False
        else:
            i += 1

    return True


if (__name__ == "__main__"):

    if(isPel(input("Enter your string: "))):
        print("Pelindrome")
    else:
        print("Not Pelindrome")
