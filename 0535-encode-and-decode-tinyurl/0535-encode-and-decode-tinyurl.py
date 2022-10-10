class Codec:
    def __init__(self):
        self.dic = {}
        self.base = 'http://tinyurl.com/'
        
    def gen_random_string(self, k):
        return ''.join(random.sample(string.ascii_letters + string.digits, k))
    

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            shortUrl = self.base + self.gen_random_string(6)
            if shortUrl not in self.dic:
                self.dic[shortUrl] = longUrl
                return shortUrl
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))