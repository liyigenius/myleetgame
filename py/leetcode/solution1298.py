from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        """
        status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]

        :param status:
        :param candies:
        :param keys:
        :param containedBoxes:
        :param initialBoxes:
        :return:
        """
        cnt = 0
        ll = []
        klist = []
        for (k,v) in enumerate(initialBoxes):

            ll.append(v)
        blist = []
        while len(ll) > 0 :
            #precheck...




            first = ll.pop(0)

            newk = keys[first]

            cnt += candies[first]
            for i in containedBoxes[first]:

                    st = status[i]
                    if st == 1:
                        ll.append(i)
                    else:
                        blist.append(i)

            for i in newk:
                klist.append(i)
            for i in klist:
                if i in blist:
                    ll.append(i)
                    blist.remove(i)
        return cnt


a = Solution()
print(a.maxCandies(         status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
 ))


