import base64
import hashlib


def encode_base64(string: str) -> str:
    """
    使用 base64 加密字符串
    """
    return base64.b64encode(string.encode('utf-8')).decode('utf-8')


def decode_base64(string: str) -> str:
    """
    使用 base64 解密字符串
    """
    return base64.b64decode(string).decode('utf-8')


def encode_md5(string: str) -> str:
    """
    使用 md5 加密字符串
    """
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def encode_sha1(string: str) -> str:
    """
    使用 sha1 加密字符串
    """
    return hashlib.sha1(string.encode('utf-8')).hexdigest()


__all__ = ['encode_base64', 'decode_base64', 'encode_md5', 'encode_sha1']
