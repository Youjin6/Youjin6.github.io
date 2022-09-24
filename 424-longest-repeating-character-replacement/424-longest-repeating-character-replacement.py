class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # 枚举每个大写字母作为 最后要该成的那个字母
        for c in range(ord('A'), ord('Z') + 1):
            j, count = 0, 0
            
            # 固定 i
            for i in range(len(s)):
                # 增加 i
                if s[i] == chr(c):
                    count += 1
                # while 来 j += 1 直到符合条件
                while i - j + 1 - count > k:
                    if s[j] == chr(c):
                        count -= 1
                    j += 1
                # 符合条件就结算 res
                res = max(res, i - j + 1)
        
        return res