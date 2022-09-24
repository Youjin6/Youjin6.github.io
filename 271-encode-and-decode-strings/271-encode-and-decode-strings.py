class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""
        for word in strs:
            ans += str(len(word)) + '#' + word
        return ans

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # now j point to the #
            length = int(s[i : j])
            ans.append(s[j + 1 : j + length + 1])
            i = j + length + 1
            
        
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))