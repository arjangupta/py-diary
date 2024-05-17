import ed25519

def generate_key_pair():
    # Generate a new key pair
    sk, vk = ed25519.create_keypair()
    return sk.to_bytes(), vk.to_bytes()

def encrypt_message(public_key, message):
    # Load the public key
    vk = ed25519.VerifyingKey(public_key)

    # Encrypt the message
    encrypted_message = vk.to_bytes() + message.encode()
    return encrypted_message

def decrypt_message(private_key, encrypted_message):
    # Load the private key
    sk = ed25519.SigningKey(private_key)

    # Decrypt the message
    vk_bytes = encrypted_message[:32]
    message = encrypted_message[32:].decode()
    if vk_bytes != sk.get_verifying_key().to_bytes():
        raise ValueError("Invalid public key")

    return message

# Example usage
private_key, public_key = generate_key_pair()
message = "Hello, world!"
encrypted_message = encrypt_message(public_key, message)
decrypted_message = decrypt_message(private_key, encrypted_message)

print("Original message:", message)
print("Decrypted message:", decrypted_message)