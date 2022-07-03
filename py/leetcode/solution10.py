from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass
        p = self.filterStar(p)
        res = self.getAns(s, p)
        return res

    @lru_cache(None)
    def getAns(self, a,b):
        if a == '' and b == '*':
            return True
        if a == '' and b == '.*':
            return True
        if a == '' and b == '':
            return True

        if a == '' and len(b) >= 2 and b[1] == '*':
            return self.getAns(a, b[2:])

        if a == '' and len(b) > 0:
            return False
        if a != '' and b == '':
            return False
        if len(b) == 1:
            if a == b or ( len(a) == 1 and  b == '.'):
                return True
            else:
                return False
        else:


            if b[1] != '*':
                if a[0] == b[0] or b[0] == '.':
                    return self.getAns(a[1:], b[1:])
            else:
                pass
                if b[0] == '.':
                    pass
                    for i in range(len(a)+1):
                        v1 = a[i:]
                        ok = self.getAns(v1, b[2:])
                        if ok:
                            return True


                else:

                    anker = b[0]
                    for i in range(len(a)):


                        if a[i] != anker:
                            break
                        else:
                            v1 = a[i+1:]
                            ok = self.getAns(v1, b[2:])
                            if ok:
                                return True
                    t1 = self.getAns(a, b[2:])
                    return t1

        return False


    def filterStar(self, w):
        ori = w
        while True:
            ori2 = ori.replace('**', '*')
            if ori2 == ori:
                break
            else:
                ori = ori2
        return ori

"""
"ssippi"
"s*p*."
"""
a = Solution()
print(a.isMatch('ippi', 'p*.'))