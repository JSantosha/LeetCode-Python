class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqdict = {}
        for i in xrange(len(nums)):
            if freqdict.get(nums[i], 0) == 0:
                freqdict[nums[i]] = 1
            else:
                freqdict[nums[i]] += 1

        sortedfreqdict = sorted(freqdict.items(), key=operator.itemgetter(1))
        result = []
        for i in xrange(k):
            result.append(sortedfreqdict[len(sortedfreqdict) - i - 1][0])

        return result