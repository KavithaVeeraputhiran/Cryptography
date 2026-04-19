
# VIGENERE CIPHER

# Encryption
def encrypt_vigenere(plain_text, key):
    result = ""
    key_index = 0
    
    for char in plain_text:
        if char >= 'A' and char <= 'Z':
            shift = ord(key[key_index]) - ord('A')
            shifted = (ord(char) - ord('A') + shift) % 26
            result = result + chr(shifted + ord('A'))
            
            key_index = key_index + 1
            if key_index == len(key):
                key_index = 0
        
        elif char >= 'a' and char <= 'z':
            shift = ord(key[key_index]) - ord('a')
            shifted = (ord(char) - ord('a') + shift) % 26
            result = result + chr(shifted + ord('a'))
            
            key_index = key_index + 1
            if key_index == len(key):
                key_index = 0
        
        else:
            result = result + char
    
    return result


# Decryption
def decrypt_vigenere(cipher_text, key):
    result = ""
    key_index = 0
    
    for char in cipher_text:
        if char >= 'A' and char <= 'Z':
            shift = ord(key[key_index]) - ord('A')
            shifted = (ord(char) - ord('A') - shift) % 26
            result = result + chr(shifted + ord('A'))
            
            key_index = key_index + 1
            if key_index == len(key):
                key_index = 0
        
        elif char >= 'a' and char <= 'z':
            shift = ord(key[key_index]) - ord('a')
            shifted = (ord(char) - ord('a') - shift) % 26
            result = result + chr(shifted + ord('a'))
            
            key_index = key_index + 1
            if key_index == len(key):
                key_index = 0
        
        else:
            result = result + char
    
    return result


# Example
text = "HELLO"
key = "KEY"

encrypted = encrypt_vigenere(text, key)
print("Encrypted:", encrypted)

decrypted = decrypt_vigenere(encrypted, key)
print("Decrypted:", decrypted)
















