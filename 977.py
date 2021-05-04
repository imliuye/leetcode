# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums):
        return sorted([a**2 for a in nums])

s = Solution()

print(s.sortedSquares([-7,-3,2,3,11]))
