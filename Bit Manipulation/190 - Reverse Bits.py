class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        t = '{:032b}'.format(n)
        x = list(t)
        rev = x[::-1]

        return int("".join(rev), 2)