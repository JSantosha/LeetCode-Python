class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        a = S.split("-")
        b = "".join(a)
        a = list(b)
        if len(a) == 0:
            return ""
        # print a
        for i in xrange(len(a)):
            if a[i] >= 'a' and a[i] <= 'z':
                a[i] = a[i].upper()
        l = []

        x = len(a) - 1
        s = ""
        count = 1
        print a
        while x >= 0:
            if count == K:
                l.append(a[x])
                l.append("-")
                count = 0
                count += 1
            else:
                l.append(a[x])
                count += 1
            x -= 1
        if l[len(s) - 1] == "-":
            l.pop()
        t = l[::-1]

        s = "".join(t)
        return s
