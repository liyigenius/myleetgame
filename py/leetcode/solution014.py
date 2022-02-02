class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        outl = ''
        if len(strs) == 0:
            return ''
        for k, v in enumerate(strs[0]):
            ok = True
            for j in range(1, len(strs)):
                if k > len(strs[j]) - 1:
                    ok = False
                    break
                ww = strs[j][k]
                if ww != v:
                    ok = False
                    break
            if ok == False:
                break
            outl += v
        return outl