from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # Primero normalizamos el password (evita límite bcrypt)
    password_bytes = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(password_bytes)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = hashlib.sha256(plain_password.encode()).hexdigest()
    return pwd_context.verify(password_bytes, hashed_password)