from IHashingFunc import IHashingFunc

class EmotetClass (IHashingFunc):

    def hashString (self, s):
        res = 0
        for c in s:
                res = (res * 0x1003f) + ord(c) & 0xffffffff
        return res