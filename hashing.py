from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_pwd, hashed_pwd):
        return pwd_context.verify(plain_pwd, hashed_pwd)

    @staticmethod
    def hash_password(password):
        return pwd_context.hash(password)
