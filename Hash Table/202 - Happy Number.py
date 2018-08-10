class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        temp = 0
        d = {}
        while True:
            while n != 0:
                x = n%10
                temp += x*x
                n = n/10
            if d.get(temp,0)==0:
                d[temp] = 1
            else:
                return False
            if temp == 1:
                return True
            n = temp
            temp = 0