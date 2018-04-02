class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        formatlist = []
        resultstring = ""
        openbrackets = []
        flag = 1
        i = 0
        l = 0
        if len(s) == 0:
            return ""

        while flag != 0:
            integer = ""
            formatlist.append(s[i])
            l = 0
            if s[i] == '[':
                openbrackets.append(i)
            if s[i] == ']':
                lastopenpos = openbrackets.pop()
                k = lastopenpos - 1
                while True:
                    if s[k].isdigit() == True:
                        integer = "".join(s[k]) + integer
                        k -= 1
                    else:
                        break

                if lastopenpos - 1 >= 0 and s[lastopenpos - 1].isdigit() == True:
                    formatlist = formatlist[:len(formatlist) - 1]
                    while True:
                        if formatlist[len(formatlist) - 1] != '[':
                            x = "".join(formatlist.pop()) + x
                        else:
                            formatlist.pop()
                            formatlist = formatlist[:len(formatlist) - len(integer)]
                            break
                    t = int(integer)
                    x = x * t
                    formatlist.append(x)
                elif lastopenpos - 1 >= 0:
                    formatlist = formatlist[:len(formatlist) - 1]
                    while True:
                        if formatlist[len(formatlist) - 1] != '[':
                            x = "".join(formatlist.pop()) + x
                        else:
                            formatlist.pop()
                            break
                    formatlist.append(x)
            if i + 1 < len(s):
                i += 1
            else:
                flag = 0
            x = ""
        result = "".join(formatlist)
        return result

