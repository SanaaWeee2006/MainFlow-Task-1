# Custom Encryption and Decryption Program

def create_substitution_cipher():
    original = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?;:"
    substitution = "QWERTYUIOPASDFGHJKLZXCVBNMmnbvcxzlkjhgfdsapoiuytrewq0987654321.,!?;:"
    return original, substitution

def substitution_encrypt(message, original, substitution):
    encrypted = ""
    for char in message:
        if char in original:
            index = original.find(char)
            encrypted += substitution[index]
        else: 
            encrypted += char
    return encrypted

def substitution_decrypt(encrypted_message, original, substitution):
    decrypted = ""
    for char in encrypted_message:
        if char in substitution:
            index = substitution.find(char)
            decrypted += original[index]
        else:
            decrypted += char
    return decrypted

def matrix_transform_encrypt(message):
    encrypted = ""
    for i in range(0, len(message), 2):
        if i + 1 < len(message):
            encrypted += message[i + 1] + message[i]
        else:
            encrypted += message[i]
    return encrypted

def matrix_transform_decrypt(encrypted_message):
    decrypted = ""
    for i in range(0, len(encrypted_message), 2):
        if i + 1 < len(encrypted_message):
            decrypted += encrypted_message[i + 1] + encrypted_message[i]
        else:
            decrypted += encrypted_message[i]
    return decrypted

def main():
    original, substitution = create_substitution_cipher()

    message = input("Enter the message to encrypt: ")

    encrypted = substitution_encrypt(message, original, substitution)
    
    encrypted = matrix_transform_encrypt(encrypted)

    print(f"\nEncrypted Message: {encrypted}")

    decrypted = matrix_transform_decrypt(encrypted)
    
    decrypted = substitution_decrypt(decrypted, original, substitution)

    print(f"\nDecrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
