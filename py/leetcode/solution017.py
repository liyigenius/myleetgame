class Solution(object):
    m1= {}
    m1['2'] = ['a','b','c']
    m1['3'] = ['d','e','f']
    m1['4'] = ['g','h','i']
    m1['5'] = ['j','k','l']
    m1['6'] = ['m','n','o']
    m1['7'] = ['p','q','r', 's']
    m1['8'] = ['t','u','v']
    m1['9'] = ['w','x','y', 'z']

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pass
        ll = []
        for i in digits:
            ll = self.yf(ll, i)
        return ll

    def yf(self, cur, w):
        ll = []
        if len(cur) == 0:
            return self.m1[w]
        for i in cur:
            for j in self.m1[w]:
                ll.append(i+j)
        return ll