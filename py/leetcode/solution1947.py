import bisect

from sortedcontainers import SortedList


class CountIntervals:

    def __init__(self):
        self.sd = SortedList(key=lambda x: (x[0]))
        self.cur = 0

    def add(self, left: int, right: int) -> None:
        if len(self.sd) == 0:
            self.sd.add((left, right))
            self.cur += right - left + 1
        else:
            lend1 = self.sd.bisect_right((left, 0))
            rend1 = self.sd.bisect_right((right, 0))
            toremoveleft = -1
            toremoveright = -1
            if lend1 == 0:
                pass
                toremoveleft = 0
            else:
                # print(self.sd[lend1-1])
                res1 = self.sd[lend1 - 1]
                if left == res1[1]:

                    # self.sd.add((left, right))
                    toremoveleft = lend1 - 1
                    left = min(left, res1[0])
                elif left > res1[1]:
                    toremoveleft = lend1
                    # self.sd.add((left, right))
                elif left < res1[1]:
                    # self.sd.remove(res1)
                    # self.sd.add((res1[0], right))
                    toremoveleft = lend1 - 1
                    left = min(left, res1[0])

            if rend1 == 0:
                pass
                toremoveright = -1
            else:
                # print(self.sd[rend1 - 1])
                res1 = self.sd[rend1 - 1]
                if right == res1[0]:
                    # self.sd.add((left, right))
                    toremoveright = rend1
                    right = max(right, res1[1])
                elif right > res1[0]:
                    toremoveright = rend1
                    # self.sd.add((left, right))
                    right = max(right, res1[1])
                elif right < res1[0]:
                    # self.sd.remove(res1)
                    # self.sd.add((res1[0], right))
                    toremoveright = rend1 - 1
            # print(toremoveleft, toremoveright)
            # ll2 = []
            # for i in range(toremoveleft, toremoveright):
            #     vv = self.sd[i]
            #     ll2.append(vv)
            # for i in ll2:
            #     self.sd.remove(i)
            #self.sd = self.sd[:toremoveleft] + self.sd[toremoveright:]
            for i in range(toremoveright-1, toremoveleft-1,-1):
                tal1 = self.sd[i]
                ans1 = tal1[1] - tal1[0] + 1
                self.cur -= ans1
                del self.sd[i]
            self.sd.add((left, right))
            self.cur += right - left + 1

    def count(self) -> int:
        pass
        return  self.cur
        # cnt = 0
        #
        # for i in self.sd:
        #     delta = i[1] - i[0] + 1
        #     cnt += delta
        # return cnt

# # Your CountIntervals object will be instantiated and called as such:
obj = CountIntervals()

# obj.add(3,5)
# obj.add(5,10)
#
obj.add(2,3)
obj.add(7,10)
obj.add(5,8)
#
# #obj.add(1,8)
#
print(obj.count())
# # obj.add(left,right)
# # param_2 = obj.count()
