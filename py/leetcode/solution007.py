class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0-2**31 or x > 2**31 - 1:
            return 0

        t = False

        a = str(x)
        if x < 0 :
            t = True
            a = a[1:]
        b = a[::-1]
        c = int(b)
        res = 0
        if t == True:
            #return 0-c
            res = 0 - c
        else:
            res = c
        if res < 0-2**31 or res > 2**31 - 1:
            return 0
        return res