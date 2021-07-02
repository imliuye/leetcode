# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
class Solution:
    def findRestaurant(self, list1, list2):
        dict1 = {list1[i]: i for i in range(len(list1))}
        result = []
        minSum = -1
        for j in range(len(list2)):
            if list2[j] in dict1:
                sum = j + dict1[list2[j]]
                if minSum == -1 or sum < minSum:
                    result = [list2[j]]
                    minSum = sum
                elif sum == minSum:
                    result += [list2[j]]
        return result


list1 = ["Shogun","Tapioca Express","Burger King","KFC"];
list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
result=['KFC', 'Burger King', 'Tapioca Express', 'Shogun']
s = Solution()
r = s.findRestaurant(list1, list2)

print(r)
