class Solution:
    def NnumbersSum(self, N):
        if N==1:
            return 1
        return N+self.NnumbersSum(N-1)

if __name__=="__main__":
    sol = Solution()
    N = 100
    ans = sol.NnumbersSum(N)
    print(ans)