import bcrypt

def get_hashed_pass(password: str):
    password_b: bytes = password.encode("utf-8")
    
    hashed_pass = bcrypt.hashpw(
        password=password_b,
        salt=bcrypt.gensalt(rounds=12)
    )

    return hashed_pass.decode("utf-8")

