from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """

        :param events:
        :return:
        """
        events.sort(key=lambda x:(x[1],x[0]))
        st = 0
        cnt = 0
        max1 = 0
        for i in events:
            if i[1] > max1:
                max1 = i[1]
        min1 = events[0][0]
        #max1 = events[-1][1]
        for i in range(min1, max1+1):
            if len(events) == 0:
                break
            if i < events[0][0]:
                continue
            if i >= events[0][0] and i <= events[0][1]:
                events.pop(0)
                cnt += 1
                continue
            while len(events) > 0:
                if i > events[0][1]:
                    events.pop(0)
                else:
                    break

            if len(events) == 0:
                break
            if i < events[0][0]:
                continue
            if i >= events[0][0]:
                events.pop(0)
                cnt += 1

        return cnt


a = Solution()
print(a.maxEvents(events =  [[1,2],[1,2],[1,6],[1,2],[1,2]] ))
