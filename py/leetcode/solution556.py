from itertools import permutations
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        t1 = [i for i in str(n)]
        qq = []
        for i in permutations(t1, len(t1)):
            qq.append(int(''.join(i)))
        #print(qq)
        qq.sort()
        index1 = qq.index(n)
        if index1 == len(qq) - 1:
            return -1
        return qq[index1+1]

a = Solution()
print(a.nextGreaterElement(2147483486))