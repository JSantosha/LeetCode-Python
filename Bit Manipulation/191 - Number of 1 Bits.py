class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = list(bin(n)[2:])
        count = 0
        for i in xrange(len(x)):
            if x[i] == '1':
                count += 1

        return count