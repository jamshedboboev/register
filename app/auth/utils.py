import jwt

from app.core.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key,
    algorithm: str = settings.auth_jwt.algorithm
):
    encoded = jwt.encode(
        payload=payload,
        key=private_key,
        algorithm=algorithm
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.auth_jwt.public_key,
    algotithm: str = settings.auth_jwt.algorithm
):
    decoded = jwt.decode(
        jwt=token,
        key=public_key,
        algorithms=[algotithm]
    )
    return decoded