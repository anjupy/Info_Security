from app.cryptography.encrypt import encrypt_data, generate_key

def test_encrypt():
    key, _ = generate_key("password")
    encrypted = encrypt_data("Hello World", key)
    assert encrypted is not None
