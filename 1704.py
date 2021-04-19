class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return len([ss for ss in s[:int(len(s) / 2)] if ss in "aeiouAEIOU"]) - \
            len([ss for ss in s[int(len(s) / 2):] if ss in "aeiouAEIOU"]) == 0


s = Solution()

print(s.halvesAreAlike('"AbCdEfGh"'))
