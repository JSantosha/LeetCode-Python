class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        temp = []
        prev = [1,1]
        for j in xrange(rowIndex-1):
            temp = [1]
            for i in xrange(len(prev)-1):
                temp.append(prev[i]+prev[i+1])
            temp.append(1)
            prev = temp
        return temp