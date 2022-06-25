from typing import List
from functools import lru_cache

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        pass
        self.m1 = {}
        for (k,v) in enumerate(parent):

            self.m1[k] = v
        print(self.m1)


    @lru_cache(None)
    def getKthAncestor(self, node: int, k: int) -> int:
        pass
        if k == 0:
            return node
        if k == -1:
            return -1
        next = self.m1.get(node, - 1)
        return self.getKthAncestor(next, k-1)



# Your TreeAncestor object will be instantiated and called as such:
obj = TreeAncestor( 7,[-1,0,0,1,1,2,2] )
res  = obj.getKthAncestor(5,2)
print(res)
# param_1 = obj.getKthAncestor(node,k)