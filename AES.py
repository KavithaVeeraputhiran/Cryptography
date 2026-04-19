# Simplified AES (Educational)

# Simple S-box (substitution table)
sbox = {
    "0": "9", "1": "4", "2": "A", "3": "B",
    "4": "D", "5": "1", "6": "8", "7": "5",
    "8": "6", "9": "2", "A": "0", "B": "3",
    "C": "C", "D": "E", "E": "F", "F": "7"
}

# XOR function for hex digits
def hex_xor(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:].upper()

# Input (4 hex digits block)
plaintext = input("Enter 4 hex digits (example 1A3F): ").upper()
key = input("Enter 4 hex digits key: ").upper()

print("\nStep 1: Plaintext:", plaintext)

# Step 2: SubBytes
substituted = ""
for ch in plaintext:
    substituted += sbox[ch]

print("Step 2: After SubBytes:", substituted)

# Step 3: ShiftRows (swap last two characters)
shifted = substituted[0] + substituted[1] + substituted[3] + substituted[2]
print("Step 3: After ShiftRows:", shifted)

# Step 4: AddRoundKey (XOR with key)
result = ""
for i in range(4):
    result += hex_xor(shifted[i], key[i])

print("Step 4: After AddRoundKey (Ciphertext):", result)

