class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = bin(num)[2:]
        count = x.count('1')
        if count != 1 or num < 0:
            return False

        index = x[::-1].find('1')

        if index % 2 != 0:
            return False

        return True
