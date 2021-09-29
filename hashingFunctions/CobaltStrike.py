## Inside the ReflectiveLoader function, CobaltStrike manually 
## finds the addresses of the following functions
##      kernel32.dll.GetProcAddress
##      kernel32.dll.VirtualAlloc
##      kernel32.dll.LoadLibraryA
##      kernel32.dll.LoadLibraryExA
##      kernel32.dll.GetModuleHandleA

max_bits = 32 

# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
 


def hashingFunction (moduleName, api):
    dllHash = 0
    # The dll is taken as Widestring, so I have to add a \x00 after each character
    dll = ''.join([c + "\x00" for c in moduleName])

    for c in dll:
        val = ord(c)
        if (val >= 0x61): # a -> A, b -> B ...
            val = val - 0x20
        dllHash = ror (dllHash, 0xD, max_bits) + val
    
    print("DLL Hash: ", hex(dllHash))
    res = 0
    for c in api:
        res = ror (res, 0xD, max_bits) + ord(c)
    
    return res + dllHash

if __name__ == "__main__":

    print (hex(hashingFunction ("wininet.dll\x00", "InternetReadFile\x00")))
