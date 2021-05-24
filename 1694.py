# [easy] https://leetcode.com/problems/reformat-phone-number/
class Solution:
    def reformatNumber(self, number: str) -> str:
        def split3(num):

            return '-'.join([ num[i:i+3] for i in range(0, len(num),3) ])
        number = number.replace('-', '').replace(' ', '')
        n,m = divmod(len(number),3)
        if n==0:
            return number;
        if m == 0 or m == 2:
            return  split3(number)
        if len(number) == 4:
            return number[:2] + '-' + number[2:]
        if m == 1:
            return split3(number[:len(number)-4]) + '-' + number[len(number)-4:len(number)-2] + '-' + number[len(number)-2:]


    def reformatNumber2(self, number: str) -> str:
        pass
        
s = Solution()
r = s.reformatNumber('33adsdf0323--3')

print(r)



