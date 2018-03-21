class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = list(bin(x))
        b = list(bin(y))
        del a[1]
        del b[1]
        al = len(a)
        bl = len(b)
        count = 0
        if al > bl:
            for i in range(al - bl):
                b.insert(0, '0')
        elif al < bl:
            for i in range(bl - al):
                a.insert(0, '0')

        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1

        return count

