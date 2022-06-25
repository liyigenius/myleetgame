class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        s = "aa", p = "a*"
        
        s = "ab", p = ".*"
        :param s:
        :param p:
        :return:
        """
        if s == p:
            return True
