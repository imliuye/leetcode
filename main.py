class Solution:
    def isOneBitCharacter1(self, bits) -> bool:
        def decodable(bb):
            #print("====bb:", bb)
            if not bb: return False
            if bb == [1]:
                return False
            if bb == [0] or bb == [1,0] or bb == [1,1]:
                return True

            remain1, remain2 = False, False

            if bb[-1] == 0:
                remain1 = decodable(bb[:-1])

            if bb[-2:] != [0,0] and bb[-2:]  != [0,1] :
                remain2 = decodable(bb[:-2])
            #print(bb, bb[:-1],bb[-1:], "remain1:",  remain1,)
            #print(bb, bb[:-2],bb[-2:] ,  "remain2:", remain2,)
            return remain1 or remain2

        return decodable(bits[:-1])


    # 用stack 做成树
    def isOneBitCharacter3(self, bits) -> bool:
        if  bits ==[0]:
            return True
        #bits.pop(-1)
        stack = [len(bits)-2]
        while stack:
            print(stack)
            index = stack.pop(0)
            if index == 0:
                if bits[index] == 0:
                    return True
            if bits[index] == 0:
                stack.append(index-1)
                if bits[index-1] == 1:
                    if index>=2:
                        stack.append(index-2)
                    else:
                        return True
            elif bits[index-1] == 1:
                if index>=2:
                    stack.append(index-2)
                else:
                    return True

        return False

    def isOneBitCharacter(self, bits) -> bool:
        if bits ==[0]:
            return True
        i = 0
        while i<len(bits):
            if bits[i] == 0:
                i += 1
            else:
                i += 2
            if i == len(bits)-1:
                return True
            if i == len(bits):
                return False

s = Solution()

print(s.isOneBitCharacter([1,1,1,0,0]))
"PAHNAPLSIIGYIR"
