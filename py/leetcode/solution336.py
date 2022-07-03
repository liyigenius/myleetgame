from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """

        :param words:
        :return:
        """
        ll = []
        for i in words:
            v2 = [j for j in i]
            v2.sort()
            v3 = ''.join(v2)
            ll.append(v3)

        print(ll)


a = Solution()
print(a.palindromePairs(words = ["abcd","dcba","lls","s","sssll"]))