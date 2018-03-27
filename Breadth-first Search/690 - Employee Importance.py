"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        vertices = []
        x = len(employees)
        imp = 0
        for i in xrange(len(employees)):
            if employees[i].id == id:
                imp += employees[i].importance
                vertices.append(employees[i].subordinates)
        if imp == 0:
            return 0
        x = len(vertices)
        while x != 0:
            for i in xrange(len(vertices[0])):
                for j in xrange(len(employees)):
                    if employees[j].id == vertices[0][i]:
                        imp += employees[j].importance
                        if len(employees[j].subordinates) != 0:
                            vertices.append(employees[j].subordinates)
                        break

            vertices.pop(0)
            x = len(vertices)

        return imp

