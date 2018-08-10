class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        stones = {}
        jewels = {}
        count = 0
        for i in xrange(len(J)):
            if jewels.get(J[i], 0) == 0:
                jewels[J[i]] = 1
            else:
                jewels[J[i]] += 1

        for i in xrange(len(S)):
            if stones.get(S[i], 0) == 0:
                stones[S[i]] = 1
            else:
                stones[S[i]] += 1

        for key in stones.keys():
            if jewels.get(key, 0) != 0:
                count += stones[key]
        return count

