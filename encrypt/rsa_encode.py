import os
import rsa


class RSA_ENCRYPT:
    def __init__(self, nbits: int = 512) -> None:
        self.public_key, self.private_key = rsa.newkeys(nbits=nbits)

    def save_rsa(self, path: str = './') -> 'RSA':
        """
        保存 私钥 和 公钥 到本地
        :param path: 保存路径
        :return:
        """
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + 'public.pem', 'wb') as f:
            f.write(self.public_key.save_pkcs1())
        with open(path + 'private.pem', 'wb') as f:
            f.write(self.private_key.save_pkcs1())
        return self

    def load_rsa(self, path: str = './') -> 'RSA':
        """
        从本地加载 私钥 和 公钥
        :param path: 加载路径
        :return:
        """
        with open(path + 'public.pem', 'rb') as f:
            self.public_key = rsa.PublicKey.load_pkcs1(f.read())
        with open(path + 'private.pem', 'rb') as f:
            self.private_key = rsa.PrivateKey.load_pkcs1(f.read())
        return self

    def encrypt(self, msg: str) -> bytes:
        """
        加密
        :param msg: 待加密的字符串
        :return: 加密后的字符串
        """
        return rsa.encrypt(msg.encode(), self.public_key)

    def decrypt(self, msg: bytes, encoding: str = 'utf-8') -> str:
        """
        解密
        :param msg: 待解密的字符串
        :param encoding: 解密后的字符串编码
        :return: 解密后的字符串
        """
        return rsa.decrypt(msg, self.private_key).decode(encoding)

    def sign(self, msg: str, hash_method: str = 'SHA-256') -> bytes:
        """
        签名
        :param msg: 待签名的字符串
        :param hash_method: 签名算法
        :return: 签名后的字符串
        """
        return rsa.sign(msg, self.private_key, hash_method)

    def verify(self, msg: str, sign: bytes) -> str:
        """
        验证签名
        :param msg: 待验证的字符串
        :param sign: 签名后的字符串
        :param hash_method: 签名方法
        :return: 返回签名算法 或者 None
        """
        try:
            verify = rsa.verify(msg, sign, self.public_key)
            return verify
        except Exception as e:
            print(e)
            return None


__all__ = ['RSA_ENCRYPT']
