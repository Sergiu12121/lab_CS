# Caesar cipher with one key
def caesar_cipher(text, key, mode="encrypt"):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    # Make sure the text is in uppercase and remove spaces
    text = text.upper().replace(" ", "")

    # Encrypt or decrypt based on the mode
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            if mode == "encrypt":
                new_idx = (idx + key) % len(alphabet)
            elif mode == "decrypt":
                new_idx = (idx - key) % len(alphabet)
            result += alphabet[new_idx]
        else:
            result += char  # non-alphabet characters are unchanged

    return result


# Example usage:
message = input("The word to be encrypted ")
key = int(input("The key "))

encrypted_message = caesar_cipher(message, key, mode="encrypt")
decrypted_message = caesar_cipher("", key, mode="decrypt")

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
