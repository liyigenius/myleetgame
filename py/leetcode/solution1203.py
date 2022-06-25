from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        ll = []
        m1 = {}
        for (k,v) in enumerate(beforeItems):
            m1[k] = v
        print(m1)
        self.mm = m1
        for i in range( n):
            res = self.popItem(i)
            print(res)


    def popItem(self, cur):
        if self.mm[cur] == []:
            return [cur]
        ll = []
        for i in self.mm[cur]:
            res1 = self.popItem(i)
            for j in res1:
                ll.append(j)
        ll.append(cur)
        return ll




a = Solution()
print(a.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
))