class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minval = []
        self.stacklist = []
        self.topoflist = -1

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stacklist.append(x)
        if len(self.minval) == 0:
            self.minval.append(x)
        elif x < self.minval[len(self.minval) - 1]:
            self.minval.append(x)
        else:
            self.minval.append(self.minval[len(self.minval) - 1])
        self.topoflist = len(self.stacklist) - 1
        print self.topoflist

    def pop(self):
        """
        :rtype: void
        """
        self.stacklist.pop()
        self.minval.pop()
        self.topoflist = len(self.stacklist) - 1

    def top(self):
        """
        :rtype: int
        """
        if self.topoflist == -1:
            return None
        return self.stacklist[self.topoflist]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minval) == 0:
            return None
        else:
            return self.minval[len(self.minval) - 1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()