from math import log,ceil,floor
class Solution:
    def findNumbers(self, nums) -> int:
        def digit(n):
            bit = floor(log(n,10))
            return bit + 1 + (n // 10 ** bit > 9)

        return len([nn for nn in nums if not digit(nn) % 2])
s = Solution()

print(s.findNumbers( [12,345,2,6,7896]  ) )
