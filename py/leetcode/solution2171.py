from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        """

        :param beans:
        :return:
        """
        beans.sort()
        delta = []
        p = 0
        for (k,v) in enumerate(beans):
            if k == 0:
                p = v
                #delta.append(p)
                continue
            else:

                delta.append(v-beans[k-1])
        print(delta)

a = Solution()
print(a.minimumRemoval(beans = [4,1,6,5]))

