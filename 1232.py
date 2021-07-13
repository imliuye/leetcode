# https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates) == 2:
            return True
        # y = Ax+B, 计算A，B
        # y1 = Ax1 + B
        # y2 = Ax2 + B
        # y1-y2 = A(x1-x2)
        # A = (y1-y2)/(x1-x2)
        # B = y1-Ax1
        # 横线或者竖线：
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        isHorizontal = x1 == x2
        isVertical = y1 == y2

        # 斜率
        # A = (y1 - y2) / (x1 - x2) if not isHorizontal else 0;
        # B = y1 - A * x1

        for i in range(3, len(coordinates)):
            x3, y3 = coordinates[i]
            # 斜率是否相同
            # A = (y1 - y2) / (x1 - x2)  = (y1 - y3) / (x1 - x3)
            print((y1 - y2) * (x1 - x3) , (x1 - x2) * (y1 - y3))
            if not (y1 - y2) * (x1 - x3) == (x1 - x2) * (y1 - y3):
                return False

        return True


s = Solution()
co = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
co=[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
co = [[1,2],[2,3],[3,5]]
result = s.checkStraightLine(co)
print(result)
