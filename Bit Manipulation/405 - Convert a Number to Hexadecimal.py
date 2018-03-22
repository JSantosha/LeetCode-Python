class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 9 and num >= 0:
            return str(num)

        d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

        if num > 0:
            x = list(bin(num)[2:])
            print x
            if len(x) % 4 != 0:
                t = 4 - ((len(x)) % 4)
                while t > 0:
                    x.insert(0, '0')
                    t -= 1
            t = 4
            s = 0
            result = ""
            print x
            while t <= len(x):
                res = int("".join(x[s:t]), 2)
                print res
                s = t
                if res <= 9 and res >= 0:
                    result += str(res)
                elif res >= 10 and res <= 15:
                    result += d[res]
                t += 4

            return result
        else:
            x = list(bin(abs(num))[2:])

            t = 32 - len(x)

            while t > 0:
                x.insert(0, '0')
                t -= 1
            for i in xrange(len(x)):
                if x[i] == '0':
                    x[i] = '1'
                else:
                    x[i] = '0'

            y = 1
            v = int("".join(x), 2)

            while y != 0:
                carry = v & y
                v = v ^ y
                y = carry << 1

            x = list(bin(abs(v))[2:])

            if len(x) % 4 != 0:
                t = (len(x) + 1) % 4
                while t >= 0:
                    x.insert(0, '0')
                    t -= 1
            t = 32 - len(x)

            while t > 0:
                x.insert(0, '1')
                t -= 1

            t = 4
            s = 0
            result = ""
            while t <= len(x):
                res = int("".join(x[s:t]), 2)
                s = t
                if res <= 9 and res >= 0:
                    result += str(res)
                elif res >= 10 and res <= 15:
                    result += d[res]
                t += 4

            return result
