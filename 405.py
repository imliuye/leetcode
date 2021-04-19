# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
class Solution:

    def toHex(self, num: int) -> str:
        s = '0123456789abcdef'
        mm = {i: s[i] for i in range(16)}

        def posHex(number):
            result = ""
            while number > 0:
                number, m = divmod(number, 16)
                print(number, m)
                result = mm[m] + result
            return result

        if num > 0:
            return posHex(num)

        return posHex(4294967296 + num)


s = Solution()

print(s.toHex(-2))
