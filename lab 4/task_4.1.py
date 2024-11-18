# DES key generation program

# Permuted Choice 1 table (PC-1)
PC1 = [
    57,
    49,
    41,
    33,
    25,
    17,
    9,
    1,
    58,
    50,
    42,
    34,
    26,
    18,
    10,
    2,
    59,
    51,
    43,
    35,
    27,
    19,
    11,
    3,
    60,
    52,
    44,
    36,
    63,
    55,
    47,
    39,
    31,
    23,
    15,
    7,
    62,
    54,
    46,
    38,
    30,
    22,
    14,
    6,
    61,
    53,
    45,
    37,
    29,
    21,
    13,
    5,
    28,
    20,
    12,
    4,
]

# Permuted Choice 2 table (PC-2)
PC2 = [
    14,
    17,
    11,
    24,
    1,
    5,
    3,
    28,
    15,
    6,
    21,
    10,
    23,
    19,
    12,
    4,
    26,
    8,
    16,
    7,
    27,
    20,
    13,
    2,
    41,
    52,
    31,
    37,
    47,
    55,
    30,
    40,
    51,
    45,
    33,
    48,
    44,
    49,
    39,
    56,
    34,
    53,
    46,
    42,
    50,
    36,
    29,
    32,
]

# Number of bit shifts for each round
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def permute(key, table):
    return [key[i - 1] for i in table]


def rotate_left(key_half, n_shifts):
    return key_half[n_shifts:] + key_half[:n_shifts]


def generate_round_keys(initial_key):
    # Apply PC-1 permutation
    permuted_key = permute(initial_key, PC1)
    print("PC-1 Permutation:", permuted_key)

    # Split the key into two halves
    C, D = permuted_key[:28], permuted_key[28:]
    print("Initial C0:", C)
    print("Initial D0:", D)

    round_keys = []
    for round_num, shifts in enumerate(SHIFT_SCHEDULE):
        # Shift each half
        C = rotate_left(C, shifts)
        D = rotate_left(D, shifts)
        print(f"After shift {round_num + 1}: C = {C}, D = {D}")

        # Combine halves and apply PC-2 permutation to get K_i
        combined_key = C + D
        K_i = permute(combined_key, PC2)
        print(f"Round {round_num + 1} Key (K_{round_num + 1}):", K_i)

        round_keys.append(K_i)

    return round_keys


def string_to_binary(key_str):
    # Convert the string to binary and ensure it's 64 bits long
    binary_key = "".join(format(ord(c), "08b") for c in key_str)

    # If the string is shorter than 8 characters (64 bits), pad it with zeroes
    if len(binary_key) < 64:
        binary_key = binary_key.ljust(64, "0")

    # Return the binary key as a list of integers (0 or 1)
    return [int(bit) for bit in binary_key]


# Input key from user
key_input = input("Enter a 8 character word key ")
transformed_key = string_to_binary(key_input)
initial_key = [int(bit) for bit in transformed_key]
round_keys = generate_round_keys(initial_key)

# Display all round keys
for i, key in enumerate(round_keys):
    print(f"K_{i + 1}: {''.join(map(str, key))}")
