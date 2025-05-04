import secrets

# Generate a 256-bit (32-byte) key for HS256
SECRET_KEY = secrets.token_hex(32)  # Hex-encoded (64 characters)

# Print the generated secret key
print("Generated secret key:")
print(SECRET_KEY)
