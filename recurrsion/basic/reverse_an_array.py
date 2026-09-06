class Solution:
    def reverse(self, arr: list, n: int) -> list:
        left = 0
        right = n-1 
        while left<right:
            arr[left],arr[right] = arr[right],arr[left]
            left +=1
            right -=1
        return arr
if __name__=="__main__":
    sol = Solution()
    l = [1,2,3,4,5,6,7]
    ans = sol.reverse(l,len(l))
    print(ans)