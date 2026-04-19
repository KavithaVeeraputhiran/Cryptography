
# Simplified DES (Educational)

# Simple permutation function
def permute(bits, order):
    result = ""
    for i in order:
        result += bits[i-1]
    return result

# XOR function
def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


# Input
plaintext = input("Enter 8-bit plaintext (example 10101010): ")
key = input("Enter 8-bit key: ")

print("\nStep 1: Initial Plaintext:", plaintext)

# Step 2: Initial Permutation
IP_order = [2,6,3,1,4,8,5,7]
plaintext = permute(plaintext, IP_order)
print("Step 2: After Initial Permutation:", plaintext)

# Step 3: Split into Left and Right
L = plaintext[:4]
R = plaintext[4:]
print("Step 3: L =", L, "R =", R)

# Step 4: Simple function (XOR R with key first 4 bits)
F = xor(R, key[:4])
print("Step 4: F function output (R XOR key):", F)

# Step 5: XOR with Left
newR = xor(L, F)
newL = R
print("Step 5: New L =", newL, "New R =", newR)

# Step 6: Combine
combined = newL + newR
print("Step 6: Before Final Permutation:", combined)

# Step 7: Final Permutation
FP_order = [4,1,3,5,7,2,8,6]
ciphertext = permute(combined, FP_order)
print("Step 7: Ciphertext:", ciphertext)
