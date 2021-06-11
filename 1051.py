# Height Checker https://leetcode.com/problems/height-checker/
class Solution:
    def heightChecker(self, heights) -> int:
        expected = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                cnt +=1
        return cnt

s = Solution()
p = [1,2,3,4,5]
r = s.heightChecker(p)

print(r)
