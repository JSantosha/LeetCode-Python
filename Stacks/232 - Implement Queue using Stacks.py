class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.back = -1
        self.front = -1
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.queue:
            self.back += 1
            self.queue.append(x)
        else:
            self.front += 1
            self.back += 1
            self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        if self.front == self.back:
            self.front = self.back = -1
            x = self.queue[self.front]
            self.queue = []
            return x
        if self.front != self.back:
            self.back -= 1
            x = self.queue[self.front]
            del self.queue[self.front]
            return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.front == -1:
            return 0
        return self.queue[self.front]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.front == self.back == -1:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()