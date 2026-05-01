from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    # Force clean input
    password = str(password)
    password = password.strip()
    
    # Safety check
    if len(password) > 72:
        password = password[:72]
    
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    plain = str(plain).strip()
    if len(plain) > 72:
        plain = plain[:72]
    return pwd_context.verify(plain, hashed)