class Solution:
    def isPalindrome(self, x: int) -> bool:
        neg = False
        if x<0:
            return neg
        x = abs(x)
        def reverse(y: int)-> int:
            rev_y = 0
            while y>0:
                rev_y = rev_y*10 + y%10
                y=y//10
            return rev_y
        rev_x = reverse(y=x)
        if x==rev_x:
            return True
        return False

if __name__=="__main__":
    sol = Solution()
    rev = sol.isPalindrome(-121)
    print(rev)