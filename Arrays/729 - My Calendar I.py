class MyCalendar(object):

    def __init__(self):
        self.res = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # print start
        # print end
        # print self.res
        for i in xrange(len(self.res)):
            temp = self.res[i]
            if start >= temp[0] and start < temp[1]:
                return False
            if end > temp[0] and end <= temp[1]:
                return False
            if start >= temp[0] and end < temp[1]:
                return False
            if temp[0] >= start and temp[0] < end and temp[1] > start and temp[1] <= end:
                return False

        self.res.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)