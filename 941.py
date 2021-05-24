# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr) -> bool:
        inc = True
        if len(arr) < 3:
            return False
        if arr[1] - arr[0] <= 0:
            return False
        incre = 0
        for i in range(1, len(arr)):
            incre = arr[i] - arr[i - 1]
            if incre == 0:
                return False

            if incre < 0 and inc:
                inc = False
                continue

            if incre > 0 and not inc:
                return False
        return not inc


s = Solution()
p = [5, 4, 3, 2]
r = s.validMountainArray(p)

print(r)
