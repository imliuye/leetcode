class Solution:
    # 尾递归
    def tribonacci(self, n: int) -> int:
        tribo = dict()
        tribo[0] = 0
        tribo[1] = 1
        tribo[2] = 1
        def _tribonacci( n: int) -> int:
            if n in tribo.keys():
                return tribo[n]
            return _tribonacci(n-3) + _tribonacci(n-2) + _tribonacci(n-1)


        return _tribonacci(n)

s = Solution()

for i in range(30):
    print(i, s.tribonacci(i))
