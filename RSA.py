# Simple RSA Implementation

# Step 1: Input two prime numbers
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

# Step 2: Compute n
n = p * q
print("\nStep 1: n = p * q =", n)

# Step 3: Compute phi(n)
phi = (p - 1) * (q - 1)
print("Step 2: phi(n) =", phi)

# Step 4: Choose e (public key)
e = int(input("Enter public key e (1 < e < phi and gcd(e,phi)=1): "))
print("Step 3: Public key (e, n) =", (e, n))

# Step 5: Find d (private key)
# d such that (d * e) % phi = 1

d = 1
while (d * e) % phi != 1:
    d += 1

print("Step 4: Private key (d, n) =", (d, n))

# Step 6: Encryption
message = int(input("\nEnter message (number): "))
cipher = (message ** e) % n
print("Step 5: Ciphertext =", cipher)

# Step 7: Decryption
decrypted = (cipher ** d) % n
print("Step 6: Decrypted message =", decrypted)
