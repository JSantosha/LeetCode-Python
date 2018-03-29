class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        nodes = [beginWord]
        lengthofword = len(beginWord)
        length = 0
        visited = set(beginWord)
        while nodes:
            nextlevel = []
            for word in nodes:
                if endWord == word:
                    return length + 1
                for j in xrange(lengthofword):
                    for k in "abcdefghijklmnopqrstuvwxyz":
                        x = word[:j] + k + word[j + 1:]
                        if x in wordList and x not in visited:
                            nextlevel.append(x)
                            visited.add(x)
            nodes = nextlevel
            length += 1

        return 0
