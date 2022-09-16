class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        res = [0] * (n + m - 1)
        ans = []
        for j in reversed(range(m)):
            for i in reversed(range(n)):
                k = i + j
                res[k] += int(num2[j]) * int(num1[i])
        print(res)
        carry = 0
        for i in reversed(res):
            carry += i
            ans.insert(0, carry % 10)
            carry //= 10
        
        if carry:
            ans.insert(0, carry)
        

        while ans and ans[0] == 0:
            ans.pop(0)
        
        
        if not ans:
            return '0'
        return ''.join(map(str, ans))
            
        
                        