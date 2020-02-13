class Solution:
    #method 1
    # Time complexity: O(n^)
    # space: 
    # Exceed time limit
    def isUnique1(self, substr: str) -> bool:
        substrSet = set(substr)
        if len(substr) != len(substrSet):
            return False
        return True
    
    def isUnique(self, substr: str) -> bool:
        substrSet = set()
        for ch in substr:
            if ch in substrSet:
                return False
            else:
               substrSet.add(ch)
        return True            
        
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        strlen = len(s)
        if strlen < 2:
            return strlen
        
        for i in range(0,strlen):
            if i + longest > strlen:
                # print("enough test")
                break
            for j in range(i+longest,strlen+1):
                substr = s[i:j]
                # print(i,j,substr);
                if not self.isUnique(substr):
                    break
                if len(substr) > longest:
                    # print("find longer:",substr)
                    longest = len(substr) 
        return longest
                
