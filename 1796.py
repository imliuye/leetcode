
class Solution:
    def secondHighest(self, s: str) -> int:
        first , sec = -1, -1

        for ss in s:
            if ss.isdigit():
                i = int(ss)

                if i > first:
                    sec = first
                    first = i

                #
                # if i >sec and i<first:
                #     sec = i
                # if sec==first:
                #     sec = i
                # print('i',i,' first:',first, ' sec:',sec)

        return sec


s = Solution()

print(s.secondHighest('"unqclirrea85188733589"'))
