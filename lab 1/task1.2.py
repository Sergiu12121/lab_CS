# Caesar cipher with two keys: permutation + shift
def caesar_cipher_permuted(text, key1, key2, mode="encrypt"):
    # Step 1: Create a permuted alphabet using key2 (like 'CRYPTOGRAPHY')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    permuted_alphabet = ""

    # First, add unique letters from key2
    for char in key2.upper():
        if char not in permuted_alphabet:
            permuted_alphabet += char

    # Then, add the remaining letters from the normal alphabet
    for char in alphabet:
        if char not in permuted_alphabet:
            permuted_alphabet += char

    result = ""

    # Step 2: Encrypt or decrypt using the permuted alphabet and key1 shift
    text = text.upper().replace(" ", "")

    for char in text:
        if char in permuted_alphabet:
            idx = permuted_alphabet.index(char)
            if mode == "encrypt":
                new_idx = (idx + key1) % len(permuted_alphabet)
            elif mode == "decrypt":
                new_idx = (idx - key1) % len(permuted_alphabet)
            result += permuted_alphabet[new_idx]
        else:
            result += char  # Non-alphabet characters are unchanged
    print(f"The permutated alphabet : {permuted_alphabet}")
    return result


# Example usage:
message = input("The word to be encrypted ")
key1 = int(input("The shift key "))  # Shift key
key2 = input("The second key ")  # Permutation key

encrypted_message = caesar_cipher_permuted(message, key1, key2, mode="encrypt")
decrypted_message = caesar_cipher_permuted(
    encrypted_message, key1, key2, mode="decrypt"
)

print(f"Original Message: {message}")
print(f"Encrypted Message with permutation: {encrypted_message}")
print(f"Decrypted Message with permutation: {decrypted_message}")
