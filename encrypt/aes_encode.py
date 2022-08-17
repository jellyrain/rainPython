from Crypto import Random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class Mode:
    """
    加密模式
    """
    ECB = AES.MODE_ECB
    CBC = AES.MODE_CBC
    CTR = AES.MODE_CTR
    CFB = AES.MODE_CFB
    OFB = AES.MODE_OFB
    OPENPGP = AES.MODE_OPENPGP
    CCM = AES.MODE_CCM
    EAX = AES.MODE_EAX
    GCM = AES.MODE_GCM
    SIV = AES.MODE_SIV
    OCB = AES.MODE_OCB


AES_MODE = Mode()


class AES_ENCRYPT:
    """
    AES加密方式使用 MODE 选择

    CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)  常用

    ECB加密不需要iv
    """

    def __init__(self, key: bytes = Random.new().read(AES.block_size), mode: int = AES_MODE.CBC, iv: bytes = Random.new().read(AES.block_size)):
        self.__key = key
        self.__mode = mode
        self.__iv = iv

    def getKey(self) -> bytes:
        """
        获取密钥
        :return: 密钥
        """
        return self.__key

    def getIV(self) -> bytes:
        """
        获取iv
        :return: iv
        """
        return self.__iv

    def encrypt(self, content: bytes) -> bytes:
        """
        加密
        :param content: 待加密的内容
        :return: 加密后的内容
        """
        cipher = AES.new(self.__key, self.__mode, self.__iv)
        return cipher.encrypt(content)

    def decrypt(self, content: bytes) -> bytes:
        """
        解密
        :param content: 待解密的内容
        :return: 解密后的内容
        """
        cipher = AES.new(self.__key, self.__mode, self.__iv)
        return cipher.decrypt(content)

    def encrypt_hex(self, content: bytes) -> str:
        """
        加密为十六进制字符串
        :param content: 待加密的内容
        :return: 加密后的内容
        """
        return b2a_hex(self.encrypt(content)).decode('utf-8')

    def decrypt_hex(self, content: str) -> bytes:
        """
        解密为原始字符串
        :param content: 待解密的内容
        :return: 解密后的内容
        """
        return self.decrypt(a2b_hex(content))

    def encrypt_str(self, content: str) -> str:
        """
        加密为十六进制字符串
        :param content: 待加密的内容
        :return: 加密后的内容
        """
        return self.encrypt_hex(content.encode('utf-8'))

    def decrypt_str(self, content: str) -> str:
        """
        解密为原始字符串
        :param content: 待解密的内容
        :return: 解密后的内容
        """
        return self.decrypt_hex(content).decode('utf-8')


__all__ = ['AES_ENCRYPT', 'AES_MODE']
