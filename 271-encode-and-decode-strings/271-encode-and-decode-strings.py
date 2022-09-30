class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ''
        for c in strs:
            ans += str(len(c)) + '#' + c
        
        return ans

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            i = j + length + 1
            ans.append(s[j + 1: i])
            
        
        return ans
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))