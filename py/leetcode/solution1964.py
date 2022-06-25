from bisect import bisect_right
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        d = list()
        ans = list()
        for ob in obstacles:
            # 这里需要改成 >=
            if not d or ob >= d[-1]:
                d.append(ob)
                ans.append(len(d))
            else:

                loc = bisect_right(d, ob)
                ans.append(loc + 1)
                d[loc] = ob
        print(d)
        return ans

a = Solution()
print(a.longestObstacleCourseAtEachPosition([5,1,5,5,1,3,4,5]))