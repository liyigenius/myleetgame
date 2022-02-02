class Solution(object):


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        l,r = 0,0
        flag = True
        c1 = ''
        m1= 0
        while flag:
            cur = s[r]
            if cur not in c1:
                c1 += cur
                if len(c1) > m1:
                    m1 = len(c1)
                r += 1
            else:
                pass
                idx = c1.find(cur)
                c1 = c1[idx+1:] + cur
                r += 1


            if r == len(s) :
                flag = False


        return m1