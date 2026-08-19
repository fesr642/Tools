import hashlib

def sha256_str(text: str) -> str:
    """输入字符串，返回sha256十六进制哈希结果"""
    byte_data = text.encode("utf-8")
    return hashlib.sha256(byte_data).hexdigest()
