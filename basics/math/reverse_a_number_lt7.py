class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x<0:
            neg = True
        x = abs(x)
        rev_x = 0
        while x>0:
            rev_x = rev_x * 10 + x%10
            x = x//10
        if neg:
            rev_x = -1*rev_x
        if rev_x<-2**31 or rev_x>2**31:
            rev_x = 0
        return rev_x


if __name__=="__main__":
    sol = Solution()
    rev = sol.reverse(123)
    print(rev)