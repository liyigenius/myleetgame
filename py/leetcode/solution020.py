class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        if len(s) == 0: return True
        for i in s:
            if i == '}' or i == ']' or i == ')':
                # check and pop..
                pass
                if len(st) == 0:
                    return False
                tmp = st.pop()
                if i == '}':
                    if tmp != '{':
                        return False
                if i == ')':
                    if tmp != '(':
                        return False
                if i == ']':
                    if tmp != '[':
                        return False

            if i == '(' or i == '[' or i == '{':
                st.append(i)
                continue

        return True if len(st) == 0 else False
