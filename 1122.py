# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1, arr2):
        counter = dict()
        index = 0
        for i in arr1:
            counter[i] = counter.get(i, 0) + 1
        for i2 in arr2:
            cnt = counter.pop(i2)
            arr1[index:index + cnt] = [i2] * cnt
            index += cnt
        ll = sorted(list(counter.keys()))
        for i3 in ll:
            cnt = counter.pop(i3)
            arr1[index:index + cnt] = [i3] * cnt
            index += cnt
        return arr1


s = Solution()

arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
arr2 = [2, 42, 38, 0, 43, 21]

# Output: [2,42,38,0,43,21,5,7,12,12,13,23,24,24,27,29,30,31,33,48]
print(s.relativeSortArray(arr1, arr2))
