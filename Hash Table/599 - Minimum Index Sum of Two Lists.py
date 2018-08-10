class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        andy = {}
        doris = {}
        for i in xrange(len(list1)):
            andy[list1[i]] = i + 1
        for i in xrange(len(list2)):
            doris[list2[i]] = i + 1
        minval = sys.maxint
        res = []
        # print doris
        # print andy
        for key in andy.keys():
            # print key
            if doris.get(key, 0) != 0:
                # print key
                sumval = doris[key] + andy[key]
                # print "Minimum value:"+str(minval)
                if sumval < minval:
                    res = []
                    minval = sumval
                    res.append(key)
                elif minval == sumval:
                    res.append(key)
                    # print res

        return res

