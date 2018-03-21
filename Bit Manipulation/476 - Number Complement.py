class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = bin(num)
        
        l = list(x[2:])
        for i in xrange(len(l)):
            if l[i] == '1':
                l[i] = '0'
            else:
                l[i] = '1'

        x = "".join(l)
        return int(x, 2)
