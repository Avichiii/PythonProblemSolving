import binascii

class Converter():
    @staticmethod
    def to_ascii(h):
        to_Aschii = binascii.unhexlify(h).decode()
        return to_Aschii

    @staticmethod
    def to_hex(s):
        s = str(s)
        # Using encode() to convert the str(s) in to  bytes and again decode() from the bytes
        to_hexa = binascii.hexlify(s.encode()).decode()
        return to_hexa


convert = Converter()
convert.to_ascii()
convert.to_hex()