
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n_s = ''
        for char in s:
            if char.isalnum():
                n_s += char
        left = 0
        right = len(n_s)-1
        while left<right:
            if n_s[left]!=n_s[right]:
                return False
            left+=1
            right-=1
        return True


if __name__=="__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    ans = sol.isPalindrome(s)
    print(ans)