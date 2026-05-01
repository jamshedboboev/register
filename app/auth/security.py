import bcrypt

from pydantic import SecretStr

def get_hashed_pass(password: str):
    password_b: bytes = password.encode("utf-8")
    
    hashed_pass = bcrypt.hashpw(
        password=password_b,
        salt=bcrypt.gensalt(rounds=12)
    )

    return hashed_pass.decode("utf-8")


def check_hash_pass(password: SecretStr, hashed_password: str):
    password_check: bool = bcrypt.checkpw(
        password.get_secret_value().encode("utf-8"),
        hashed_password.encode("utf-8")
    )

    return password_check