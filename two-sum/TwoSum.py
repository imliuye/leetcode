class Solution:
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time complexity: O(N^)
        # Space complexity: O(1)
        for i in range(0,len(nums)):
            if target-nums[i] in nums[i+1:]:
                return [i,nums[i+1:].index(target-nums[i])+i+1]
    
    #use a set to store the complement
    def twoSum(self,nums, target):
        compSet = {i:(target - nums[i]) for i  in range(0,len(nums)}
        print  (compSet)
        for i in range(0,len(nums)):
            comp = target - nums[i]
            if comp in compSet and nums[i] != comp :
                return [i,nums.index(comp)]
            
