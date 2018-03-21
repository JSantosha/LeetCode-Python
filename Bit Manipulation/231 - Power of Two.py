class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        x = bin(n)[2:]
        count = x.count('1')
        if count == 1 and n >= 0:
            return True
        return False
