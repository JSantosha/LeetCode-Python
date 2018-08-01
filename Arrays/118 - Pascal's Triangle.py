class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        numRows -= 2
        prevrow = [1, 1]
        while numRows > 0:
            temp = [1]
            i = 0
            while i + 1 != len(prevrow):
                temp.append(prevrow[i] + prevrow[i + 1])
                i += 1
            temp.append(1)
            result.append(temp)
            prevrow = temp
            numRows -= 1

        return result