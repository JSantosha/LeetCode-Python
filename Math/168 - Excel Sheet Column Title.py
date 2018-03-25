class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = n
        s = ""
        if i <= 26:
            return chr(i-1+65)
        else:
            if i%26 != 0:
                while i >26:
                    t = i%26
                    i = i/26
                    s = chr(t-1+65)+s
                s = chr(i-1+65)+s
            else:
                while i >=26:
                    t = 26
                    i = (i-26)/26
                    print t
                    s = chr(t-1+65)+s
                if i != 0:
                    s = chr(i-1+65)+s
        return s
