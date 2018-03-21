class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        b = []
        for i in xrange(L, R + 1):
            b.append(bin(i)[2:].count("1"))
        count = 0
        flag = 0
        for i in xrange(len(b)):
            j = 0
            flag = 0
            if b[i] == 1:
                continue
            for j in xrange(2, int(math.sqrt(b[i])) + 1):
                if b[i] % j == 0:
                    flag = 1
                    break
            if flag == 0:
                count += 1

        return count