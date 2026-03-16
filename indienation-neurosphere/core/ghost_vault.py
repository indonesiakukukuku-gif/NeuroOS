import os
from cryptography.fernet import Fernet

# @path: ~/indienation-neurosphere/core/ghost_vault.py
# @authority: IID-021+

KEY_PATH = os.path.expanduser("~/indienation-neurosphere/core/.vault.key")

def generate_or_load_key():
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as key_file:
            key_file.write(key)
        # Sembunyikan file kunci dengan akses terbatas
        os.chmod(KEY_PATH, 0o400) 
        return key
    return open(KEY_PATH, "rb").read()

def encrypt_data(data_string):
    f = Fernet(generate_or_load_key())
    return f.encrypt(data_string.encode()).decode()

def decrypt_data(encrypted_string):
    f = Fernet(generate_or_load_key())
    return f.decrypt(encrypted_string.encode()).decode()

if __name__ == "__main__":
    # Test Enkripsi untuk Identitas IID-021+
    secret = "Flight S6: Berlin-Direct | Budget S25: 50000 EUR"
    encrypted = encrypt_data(secret)
    print(f"🔒 [VAULT] Data Terenkripsi: {encrypted[:30]}...")
    print(f"🔓 [VAULT] Data Terdekripsi: {decrypt_data(encrypted)}")
