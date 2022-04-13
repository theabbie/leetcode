class Codec:

    def encode(self, longUrl: str) -> str:
        return longUrl
        

    def decode(self, shortUrl: str) -> str:
        return shortUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))