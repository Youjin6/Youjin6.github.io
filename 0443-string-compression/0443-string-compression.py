class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        n = len(chars)
        c = chars[0]
        
        while r < n:
            count = 0
            while r < n and chars[r] == c:
                r += 1
                count += 1
            
            if count > 1:
                length = str(count)
                for i in range(len(length)):
                    chars[l + 1 + i] = length[i]
                l += len(length)
            
            l += 1
            if r < n:
                c = chars[r]
                chars[l] = c
                
            
        return len(chars[:l])