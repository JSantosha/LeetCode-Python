class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if len(graph) == 1 or len(graph) == 2:
            return True
        nodes = [[0]]
        visited = []
        nextlevel = []
        colorcodes = {}
        c = 'R'
        length = 0
        flag = 0
        t = [i for i in xrange(len(graph))]
        while nodes:
            for i in xrange(len(nodes)):
                for j in xrange(len(nodes[i])):
                    if nodes[i][j] not in visited:
                        visited.append(nodes[i][j])
                        t[nodes[i][j]] = -1
                        colorcodes[nodes[i][j]] = c
                        if len(graph[nodes[i][j]]) != 0:
                            nextlevel.append(graph[nodes[i][j]])
                    else:
                        if colorcodes.get(nodes[i][j], 0) != 0:
                            if colorcodes[nodes[i][j]] != c:
                                return False
            nodes = []
            length += 1
            if len(nextlevel) == 0 and len(visited) != len(graph):
                for k in xrange(len(t)):
                    if t[k] >= 0:
                        nodes = [[t[k]]]
                        break
            else:
                nodes = nextlevel
            if flag == 1:
                break
            visited.sort()
            nextlevel = []

            if len(visited) == len(graph):
                flag = 1
            if c == 'R':
                c = 'B'
            else:
                c = 'R'

        return True
