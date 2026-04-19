# Diffie-Hellman Key Exchange

# Step 1: Public values
p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))

print("\nPublic values: p =", p, ", g =", g)

# Step 2: Private keys
a = int(input("Enter private key of User A: "))
b = int(input("Enter private key of User B: "))

# Step 3: Compute public keys
A = (g ** a) % p
B = (g ** b) % p

print("\nStep 1: Public key of A =", A)
print("Step 2: Public key of B =", B)

# Step 4: Shared secret
secret_A = (B ** a) % p
secret_B = (A ** b) % p

print("\nStep 3: Secret key computed by A =", secret_A)
print("Step 4: Secret key computed by B =", secret_B)