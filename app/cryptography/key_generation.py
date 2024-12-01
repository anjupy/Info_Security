from Crypto.PublicKey import RSA

# Function to generate RSA keys
def generate_rsa_keys(key_size=2048):
    key = RSA.generate(key_size)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_key)
    
    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_key)
    
    print("RSA keys generated and saved as 'private_key.pem' and 'public_key.pem'.")
