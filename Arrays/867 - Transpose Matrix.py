class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose = []
        for j in xrange(len(A[0])):
            newrow = []
            for i in xrange(len(A)):
                newrow.append(A[i][j])
            transpose.append(newrow)

        return transpose