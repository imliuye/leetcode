class Solution:
    def decompressRLElist(self, nums):
        result = []
        for i in range(int(len(nums) / 2)):
            freq,val = nums[2*i], nums[2*i+1]
            result += [val] * freq
        return result

nums = [1,1,2,3,4,5]
s = Solution()
r = s.decompressRLElist(nums)

print(r)
