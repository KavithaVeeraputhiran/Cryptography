# HILL CIPHER (n x n MATRIX)
# Only works for uppercase letters

# Function to convert letter to number (A=0, B=1, ..., Z=25)
def char_to_num(c):
    return ord(c) - ord('A')

# Function to convert number to letter
def num_to_char(n):
    return chr(n + ord('A'))

# Function to multiply matrix and vector
def multiply_matrix_vector(matrix, vector, n):
    result = [0] * n
    
    for i in range(n):
        total = 0
        for j in range(n):
            total = total + matrix[i][j] * vector[j]
        result[i] = total % 26
    
    return result


# Function to find determinant (recursive)
def determinant(matrix, n):
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    for c in range(n):
        submatrix = []
        for i in range(1, n):
            row = []
            for j in range(n):
                if j != c:
                    row.append(matrix[i][j])
            submatrix.append(row)
        
        sign = (-1) ** c
        det = det + sign * matrix[0][c] * determinant(submatrix, n-1)
    
    return det


# Function to find modular inverse of a number mod 26
def mod_inverse(a):
    a = a % 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return -1


# Function to get cofactor matrix
def cofactor_matrix(matrix, n):
    cof = []
    
    for i in range(n):
        row = []
        for j in range(n):
            submatrix = []
            for r in range(n):
                if r != i:
                    temp_row = []
                    for c in range(n):
                        if c != j:
                            temp_row.append(matrix[r][c])
                    submatrix.append(temp_row)
            
            sign = (-1) ** (i + j)
            row.append(sign * determinant(submatrix, n-1))
        
        cof.append(row)
    
    return cof


# Function to transpose matrix
def transpose(matrix, n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        result.append(row)
    return result


# Function to find inverse of matrix mod 26
def inverse_matrix(matrix, n):
    det = determinant(matrix, n)
    det = det % 26
    
    det_inv = mod_inverse(det)
    if det_inv == -1:
        print("Matrix is not invertible")
        return None
    
    cof = cofactor_matrix(matrix, n)
    adj = transpose(cof, n)
    
    inv = []
    for i in range(n):
        row = []
        for j in range(n):
            value = adj[i][j] * det_inv
            row.append(value % 26)
        inv.append(row)
    
    return inv


# Encryption
def encrypt_hill(plain_text, key_matrix, n):
    result = ""
    
    # Padding with 'X' if needed
    while len(plain_text) % n != 0:
        plain_text = plain_text + 'X'
    
    for i in range(0, len(plain_text), n):
        block = plain_text[i:i+n]
        vector = []
        
        for char in block:
            vector.append(char_to_num(char))
        
        encrypted_vector = multiply_matrix_vector(key_matrix, vector, n)
        
        for num in encrypted_vector:
            result = result + num_to_char(num)
    
    return result


# Decryption
def decrypt_hill(cipher_text, key_matrix, n):
    result = ""
    
    inv_matrix = inverse_matrix(key_matrix, n)
    if inv_matrix is None:
        return ""
    
    for i in range(0, len(cipher_text), n):
        block = cipher_text[i:i+n]
        vector = []
        
        for char in block:
            vector.append(char_to_num(char))
        
        decrypted_vector = multiply_matrix_vector(inv_matrix, vector, n)
        
        for num in decrypted_vector:
            result = result + num_to_char(num)
    
    return result


# Example
key = [
    [3, 3],
    [2, 5]
]

n = 2
text = "HELP"

encrypted = encrypt_hill(text, key, n)
print("Encrypted:", encrypted)

decrypted = decrypt_hill(encrypted, key, n)
print("Decrypted:", decrypted)