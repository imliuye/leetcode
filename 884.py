class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        count = dict()

        for w in A.split(' '):
            count[w] = count.get(w,0) + 1
        for w in B.split(' '):
            count[w] = count.get(w,0) + 1
        return [w for w in count.keys() if count[w]==1]

s = Solution()

print(s.uncommonFromSentences("this apple is sweet", "this apple is sour"));
