class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}
        self.priority = {}
        self.count = 0
        self.length = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.d.get(key):
            self.priority[key] = self.count
            self.count += 1
            return self.d[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self.d) != self.length:
            self.d[key] = value
            self.priority[key] = self.count
            self.count += 1
        elif len(self.d) == self.length:
            if self.get(key) != -1:
                self.d[key] = value
                self.priority[key] = self.count
                self.count += 1
            else:
                minval = sys.maxint
                t = 0
                for key1 in self.d.keys():
                    if self.priority[key1] < minval:
                        t = key1
                        minval = self.priority[key1]
                self.d.pop(t)
                self.priority.pop(t)
                self.d[key] = value
                self.priority[key] = self.count
                self.count += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)