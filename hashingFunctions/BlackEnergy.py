from IHashingFunc import IHashingFunc

# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

class BlackEnergyClass (IHashingFunc):

    def hashString (self, data):
        res = 0
        for c in data:
            res = ord(c) ^ rol (res, 7, 32)
        
        return res 