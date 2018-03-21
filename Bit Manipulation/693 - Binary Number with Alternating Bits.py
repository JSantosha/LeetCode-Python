class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        l = list(bin(n)[2:])
        if len(l) == 1:
            return True

        for i in xrange(1, len(l)):
            if l[i - 1] == l[i]:
                return False

        return True
