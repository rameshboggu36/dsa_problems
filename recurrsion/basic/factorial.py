class Solution:
    def factorial(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        return n*self.factorial(n-1)
    def factorial_without_recursion(self, n: int)-> int:
        result = 1
        if n==0 or n==1:
            result =  1
        for i in range(2,n+1):
            result *= i
        return result

if __name__=="__main__":
    sol = Solution()
    n = 5
    ans = sol.factorial(n)
    print(ans)
    ansb = sol.factorial_without_recursion(n)
    print(ansb)