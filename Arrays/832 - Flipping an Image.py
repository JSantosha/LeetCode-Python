class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in xrange(len(A)):
            A[i] = A[i][::-1]

        for i in xrange(len(A)):
            for j in xrange(len(A[i])):
                A[i][j] ^= 1
        return A