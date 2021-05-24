# https://leetcode.com/problems/duplicate-zeros/
class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        old_len = len(arr)
        zeros = [i for i in arr if i == 0]
        new_len = len(arr) + len(zeros)

        def swap(i, j):
            if j >= len(arr):

                arr[i], zeros[j - len(arr)] = zeros[j - len(arr)], arr[i]
            else:
                arr[i], arr[j] = arr[j], arr[i]

        while old_len > 0:
            old_len -= 1
            new_len -= 1
            if arr[old_len] == 0:
                new_len -= 1
            swap(old_len, new_len)


arr = [1, 0, 2, 3, 0, 4, 5, 0]
s = Solution()
r = s.duplicateZeros(arr)
print(arr)
