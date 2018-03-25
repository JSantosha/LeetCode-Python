class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        while num != 0:
            result = result + num % 10
            num = num / 10
            if num == 0 and result >= 10:
                num = result
                result = 0

        return result

