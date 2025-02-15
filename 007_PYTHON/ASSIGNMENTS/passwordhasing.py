#Write a hashing script using the hashlib library to secure passwords.

import hashlib
import os

def hash_password(password):
    """Hashes a password with a random salt using SHA-256."""
    salt = os.urandom(32)  # Generate a 32-byte random salt
    hash_obj = hashlib.sha256(salt + password.encode())  # Hash password + salt
    password_hash = hash_obj.hexdigest()
    return salt.hex() + ":" + password_hash  # Store salt and hash together

def verify_password(stored_hash, password):
    """Verifies a password against the stored hash."""
    salt, hashed_password = stored_hash.split(":")  # Split salt and hash
    salt = bytes.fromhex(salt)  # Convert salt back to bytes
    new_hash = hashlib.sha256(salt + password.encode()).hexdigest()  # Hash input password
    return new_hash == hashed_password  # Compare hashes

if __name__ == "__main__":
    user_password = input("Enter password to hash: ")
    hashed = hash_password(user_password)
    print(f"Stored Hash: {hashed}")

    # Verify Password
    password_attempt = input("Re-enter password to verify: ")
    if verify_password(hashed, password_attempt):
        print("✅ Password is correct!")
    else:
        print("❌ Password is incorrect.")
