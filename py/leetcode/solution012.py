class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                   30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC',
                   300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM',
                   3000: 'MMM'}
        bit = num % 10
        ten = (num % 100) // 10
        hundredth = (num % 1000) // 100
        thousand_bit = num // 1000
        a = symbol[thousand_bit*1000] + symbol[hundredth*100] + symbol[ten*10] + symbol[bit*1]
        return a