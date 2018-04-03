class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if len(temperatures) == 0:
            return []
        waitdays = [0 for i in xrange(len(temperatures))]
        stack = [temperatures[0]]
        index = 0
        indexlist = [0]
        for i in xrange(1, len(temperatures)):
            if stack:
                if stack[-1] >= temperatures[i]:
                    stack.append(temperatures[i])
                    indexlist.append(i)
                elif stack[-1] < temperatures[i]:
                    j = len(indexlist) - 1
                    while j >= 0:
                        waitdays[indexlist[j]] = i - indexlist[j]
                        stack.pop()
                        indexlist.pop()
                        if len(stack) == 0 or stack[-1] >= temperatures[i]:
                            break
                        j -= 1
                    stack.append(temperatures[i])
                    indexlist.append(i)

            else:
                stack.append(temperatures[i])
                indexlist.append(i)
        return waitdays



