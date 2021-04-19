class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        if k<2:return True
        length = m*k
        def checkPattern(startIndex):
            firstPattern = arr[startIndex:startIndex+m]
            print('first:', firstPattern)
            for j in range(startIndex+m,startIndex+length, m):
                print('j:',j)
                nextPattern =arr[j:j+m];
                print('j:',j,', nextPattern', nextPattern)

                if firstPattern != nextPattern:
                    return False
            return True
            pass

        for i in range(len(arr)-length+1):
            print("\n### i:",i)
            if checkPattern(i):
                return True

s = Solution()

print(s.containsPattern([3,6,6,6,5,1,5,2,2,3,1,5,2,6,1,5,1,2,6,3,3,5,3,6,3,4],6,2))
