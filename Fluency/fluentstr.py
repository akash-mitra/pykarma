class FluentStr:

    """
    # 1
    Get the length of a string
    without using any library function
    """
    def string_len(self, string):
        count = 0
        for i in string:
            count += 1
        return count



    """
    # 2
    Reverse a string
    """
    def string_reverse(self, string):
        return string[::-1]


    """
    # 3
    Search if a substring is
    present in another string
    """
    def sunstr(self, heystack, needle):
        
