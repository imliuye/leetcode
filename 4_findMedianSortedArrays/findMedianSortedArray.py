class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        m = len(nums1)
        n = len(nums2)
        return 0

if __name__ == '__main__':
    s = Solution()
    num1 = [1,3,8,9,15]
    num2 = [7,11,18,19,21,25]
    result = s.findMedianSortedArrays(num1, num2)
    print(result)
