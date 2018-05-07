class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        result = []
        count = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                heapq.heappush(result, matrix[i][j])

        heapq.heapify(result)
        for i in xrange(k - 1):
            heapq.heappop(result)

        return heapq.heappop(result)


