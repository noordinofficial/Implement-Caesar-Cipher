# Function to encrypt text using Caesar Cipher
def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)

# User input for message and shift
message = input("Enter the message: ")
shift = int(input("Enter shift value: "))

# Encrypting and decrypting the message
encrypted_message = encrypt_caesar(message, shift)
decrypted_message = decrypt_caesar(encrypted_message, shift)

print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
