"""
271. Encode and Decode Strings

"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        st = ""
        for i in strs:
            st = st + "$"+str(len(i))+"$"+i
        return st

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i< len(s):
            number = 0
            i += 1
            while s[i] is not "$":
                number = number*10 + int(s[i])
                i += 1
            i += 1
            start = i
            ts = ""
            while i-start < number:
                ts += s[i]
                i += 1
                
            res.append(ts)
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
