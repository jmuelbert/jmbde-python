# security.py
from typing import Optional

from cryptography.fernet import Fernet


class SecurityManager:
    def __init__(self, key: Optional[bytes] = None):
        self._key = key or Fernet.generate_key()
        self._fernet = Fernet(self._key)

    def encrypt_data(self, data: str) -> bytes:
        return self._fernet.encrypt(data.encode())

    def decrypt_data(self, encrypted_data: bytes) -> str:
        return self._fernet.decrypt(encrypted_data).decode()
