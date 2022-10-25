class Solution:
    """
        
        a a b b c c c
        a 2 b 2 c 3     
        """
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        n = len(chars)
        if len(chars) == 1:
            return 1
        char = chars[0]
        while l < n and r < n:
            count = 0
            while r < n and chars[r] == char:
                r += 1
                count += 1
            if count > 1:
                num = str(count)
                for i in range(len(num)):
                    chars[l + 1 + i] = num[i]
                l += len(num) + 1
            else:
                l += 1
            if r < n:
                char = chars[r]
                chars[l] = char
        
        
        return len(chars[:l])
            