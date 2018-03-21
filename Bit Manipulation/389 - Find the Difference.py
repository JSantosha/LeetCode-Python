class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        old = list(s)
        new = list(t)
        print old
        print new

        o = []
        n = []
        result = 0
        for i in xrange(len(old)):
            result = result ^ ord(old[i])

        for i in xrange(len(new)):
            result = result ^ ord(new[i])

        return chr(result)