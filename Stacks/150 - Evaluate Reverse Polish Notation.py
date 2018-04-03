class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #This Code works for python 3 versions and causes differences in division for python 2.
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit() == True:
                stack.append(int(tokens[i]))
            elif tokens[i] == '+':
                result = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '-':
                result = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '/':
                result = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '*':
                result = (stack[-1] * stack[-2])
                stack.pop()
                stack.pop()
                stack.append(result)
        return stack[0]
