class Solution:
    def compress(self, chars: List[str]) -> int:
        cur, r = 0, 0
        n = len(chars)
        c = chars[0]
        
        while cur< n  and r < n:
            count = 0
            while r < n and chars[r] == c:
                r += 1
                count += 1
            
            if count > 1:
                length = str(count)
                for i in range(len(length)):
                    chars[cur + 1 + i] = length[i]
                cur += len(length)
            
            cur += 1
            if r < n:
                c = chars[r]
                chars[cur] = c
                
            
        return len(chars[:cur])