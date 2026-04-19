# SHIFT CIPHER (CAESAR CIPHER)

# Encryption
def encrypt_shift(plain_text, key):
    result = ""
    
    for char in plain_text:
        # Encrypt uppercase letters
        if char >= 'A' and char <= 'Z':
            shifted = (ord(char) - ord('A') + key) % 26
            result = result + chr(shifted + ord('A'))
        
        # Encrypt lowercase letters
        elif char >= 'a' and char <= 'z':
            shifted = (ord(char) - ord('a') + key) % 26
            result = result + chr(shifted + ord('a'))
        
        else:
            result = result + char   # Keep spaces and symbols unchanged
    
    return result


# Decryption
def decrypt_shift(cipher_text, key):
    result = ""
    
    for char in cipher_text:
        if char >= 'A' and char <= 'Z':
            shifted = (ord(char) - ord('A') - key) % 26
            result = result + chr(shifted + ord('A'))
        
        elif char >= 'a' and char <= 'z':
            shifted = (ord(char) - ord('a') - key) % 26
            result = result + chr(shifted + ord('a'))
        
        else:
            result = result + char
    
    return result


# Example
text = "HELLO"
key = 3

encrypted = encrypt_shift(text, key)
print("Encrypted:", encrypted)

decrypted = decrypt_shift(encrypted, key)
print("Decrypted:", decrypted)
