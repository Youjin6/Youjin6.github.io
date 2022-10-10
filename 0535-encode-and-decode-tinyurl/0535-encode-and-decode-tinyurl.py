class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = 'http://tinyurl.com/'
        
    def gen_random_string(self, k):
        return ''.join(random.sample(string.ascii_letters + string.digits, k))
    

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            shortUrl = self.base + self.gen_random_string(6)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))