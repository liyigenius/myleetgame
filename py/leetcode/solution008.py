class Solution:
    def myAtoi(self, s: str) -> int:
        """

        :param s:
        :return:
        """
        start = ''
        signed = None
        for (k,v) in enumerate(s):
            if v == ' ':
                if signed is None:
                    continue
                else:
                    pass#calc res..
                    return self.getRes(start, signed)

            if v == '+':
                if signed is None:
                    signed = 1
                    continue
                else:
                    return self.getRes(start, signed)
            if v == '-':
                if signed is None:
                    signed = -1
                    continue
                else:
                    return self.getRes(start, signed)
            if v.isdigit():
                if signed is None:
                    signed = 1
                    start += v
                else:
                    start += v
            else:
                pass
                return self.getRes(start, signed)
        if start != '':
            return self.getRes(start, signed)
        return 0

    def getRes(self, n, signed):
        if n == '':
            return 0
        n = int(n)*signed
        if n < 0-2**31:
            return 0-2**31
        if n > 2**31-1:
            return 2**31-1
        return int(n)

a = Solution()
print(a.myAtoi("words and 987"))