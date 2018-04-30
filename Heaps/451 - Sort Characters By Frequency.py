class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        chardict = {}

        for i in xrange(len(s)):
            if chardict.get(s[i], 0) == 0:
                chardict[s[i]] = 1
            else:
                chardict[s[i]] += 1

        sortedchardicts = sorted(chardict.items(), key=operator.itemgetter(1))
        result = ''
        for i in xrange(len(sortedchardicts)):
            result += sortedchardicts[i][0] * sortedchardicts[i][1]

        return result[::-1]