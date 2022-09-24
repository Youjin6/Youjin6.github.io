class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        postfix = [0] * n
        postfix[-1] = nums[-1]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in reversed(range(0, n - 1)):
            postfix[i] = postfix[i + 1] * nums[i] 
        
        ans = [0] * n
        ans[0] = postfix[1]
        ans[-1] = prefix[n - 2]
        for i in range(1, n - 1):
            ans[i] = prefix[i - 1] * postfix[i + 1]
        return ans
        

        """
        
        nums= [1,      2,       3,      4]
               1*2*3*4  1*3*4   1*2*4   1*2*3*1  
        
        
        """