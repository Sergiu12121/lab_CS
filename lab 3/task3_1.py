# Function to clean the text and ensure only allowed characters are used
def clean_text(text):
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZĂÂÎȘȚabcdefghijklmnopqrstuvwxyzăâîșț")
    if not all(ch in valid_chars for ch in text):
        raise ValueError("Text must only contain letters from the Romanian alphabet.")

    # Convert to uppercase and replace 'J' with 'I'
    cleaned_text = text.upper().replace("J", "I")
    return cleaned_text


# Function to prepare text for encryption/decryption
def prepare_text(text):
    text = clean_text(text)
    prepared = ""
    i = 0
    while i < len(text):
        prepared += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared += (
                "X"  # Add padding character if there are duplicate letters in a pair
            )
        i += 1
    if len(prepared) % 2 != 0:
        prepared += "X"  # Padding if odd length
    return prepared


# Function to create a Playfair key matrix with 5x6 dimensions
def create_key_matrix(key):
    key = clean_text(key)
    if len(key) < 7:
        raise ValueError("The key must be at least 7 characters long.")

    seen = set()
    matrix = []
    for char in key:
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    # Romanian alphabet with "J" replaced by "I" in this matrix 
    alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
    for char in alphabet:
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    return [matrix[i : i + 6] for i in range(0, 30, 6)]


# Function to find the position of a character in the matrix 
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    raise ValueError(f"Character '{char}' not found in matrix")


# Function to process pairs for encryption/decryption 
def process_pairs(text, matrix, encrypt=True):
    result = ""
    step = 1 if encrypt else -1

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row
            result += matrix[row1][(col1 + step) % 6]
            result += matrix[row2][(col2 + step) % 6]
        elif col1 == col2:  # Same column
            result += matrix[(row1 + step) % 5][col1]
            result += matrix[(row2 + step) % 5][col2]
        else:  # Rectangle swap
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


# Main function for encryption/decryption
def playfair_cipher():
    operation = input("Choose operation (en/de): ").strip().lower()
    if operation not in ["en", "de"]:
        print("Invalid operation. Please choose 'en' or 'de'.")
        return

    key = input("Enter the key (at least 7 characters): ").strip()
    matrix = create_key_matrix(key)

    if operation == "en":
        message = input("Enter the message to encrypt: ").strip()
        prepared_text = prepare_text(message)
        result = process_pairs(prepared_text, matrix, encrypt=True)
        print("Encrypted message:", result)
    else:
        cryptogram = input("Enter the cryptogram to decrypt: ").strip()
        prepared_text = prepare_text(cryptogram)
        result = process_pairs(prepared_text, matrix, encrypt=False)
        print("Decrypted message:", result)


if __name__ == "__main__":
    try:
        playfair_cipher()
    except ValueError as ve:
        print(ve)
