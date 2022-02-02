class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        ok = True
        for i in range(0, len(a) / 2):
            if a[i] != a[len(a) - i - 1]:
                ok = False
                break

        return ok