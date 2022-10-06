def str2hex(text: str):
    ret = ""
    for x in text:
        charHexStr = hex(ord(x))[2:]
        if len(charHexStr) == 3:
            charHexStr = "0" + charHexStr
        elif len(charHexStr) == 2:
            charHexStr = "00" + charHexStr
        ret += charHexStr
    return ret


def hex2str(text: str):
    ret = ""
    for i in range(0, len(text), 4):
        unicodeHexStr = text[i:i + 4]
        charStr = chr(int(unicodeHexStr, 16))
        ret += charStr
    return ret


class Beast:

    def __init__(self, beastDictArr):
        self.beastDictArr = beastDictArr

    def toBeast(self, rawStr):
        tfArray = list(str2hex(rawStr))
        beast = ""
        n = 0
        for x in tfArray:
            k = int(x, 16) + n % 16
            if k >= 16:
                k -= 16
            beast += self.beastDictArr[int(k / 4)] + self.beastDictArr[k % 4]
            n += 1
        return f'{self.beastDictArr[3]}{self.beastDictArr[1]}{self.beastDictArr[0]}{beast}{self.beastDictArr[2]}'

    def fromBeast(self, decoratedBeastStr):
        beastStr = decoratedBeastStr[3:-1]
        beastCharArr = list(beastStr)
        unicodeHexStr = ""
        for i in range(0, len(beastCharArr), 2):
            pos1 = self.beastDictArr.index(beastCharArr[i])
            pos2 = self.beastDictArr.index(beastCharArr[i + 1])
            k = ((pos1 * 4) + pos2) - (int(i / 2) % 16)
            if k < 0:
                k += 16
            unicodeHexStr += hex(k)[2:]
        return hex2str(unicodeHexStr)


__all__ = ['Beast']
