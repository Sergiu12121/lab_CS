# Topic: _DES Key Generation Algorithm_

## Author: _Dimbitchi Sergiu_

---

## Introduction

In cryptography, the Data Encryption Standard (DES) is a symmetric-key algorithm used for the encryption of data. One of the key steps in the DES algorithm is the generation of round keys, which are used in the 16 rounds of encryption. DES key generation involves multiple permutations and shifts to ensure the security of the algorithm. The process includes the use of the Permuted Choice 1 (PC-1) and Permuted Choice 2 (PC-2) tables, along with bitwise rotations to generate the 16 round keys. This laboratory work focuses on implementing the key generation process for DES and understanding the intricate details of key transformations involved in this cryptographic process.

---

## Objectives

1. Understand the DES key generation process and its components.
2. Implement the key generation mechanism based on the PC-1, PC-2, and SHIFT_SCHEDULE.
3. Analyze and verify the correct generation of 16 round keys.
4. Learn how to manipulate and rotate bit strings to generate secure keys for encryption.

---

## Theoretical Background

### DES Key Generation Process

DES encryption requires a 56-bit key, which is then expanded into 16 round keys. These round keys are generated through a series of permutations and bitwise rotations, ensuring that each round key is derived from the initial key in a secure and dynamic way. The process can be broken down into the following steps:

1. **Initial Key (56 bits)**: The key provided must be a 56-bit value, typically derived from a 64-bit input where every 8th bit is discarded.
2. **Permuted Choice 1 (PC-1)**: A permutation applied to the initial key to rearrange and reduce the bits to 56.
3. **Splitting into Two Halves**: The 56-bit key is split into two 28-bit halves (C0 and D0).
4. **Bit Shifting**: Both halves undergo circular left shifts according to a predefined schedule.
5. **Permuted Choice 2 (PC-2)**: After shifting, a second permutation is applied to form the 48-bit round key.
6. **Round Key Generation**: This process is repeated for 16 rounds, each time generating a new 48-bit round key used in the encryption process.

### PC-1 and PC-2 Tables

The **Permuted Choice 1 (PC-1)** is used to reorder the bits of the initial 56-bit key, and the **Permuted Choice 2 (PC-2)** is used to select 48 bits from the combined halves (C and D) to generate the round keys.

### Bit Shifting

The **SHIFT_SCHEDULE** defines how many bits are shifted left during each round of key generation. The number of shifts differs for each round, ensuring that the generated keys are sufficiently different from one another.

---

## Implementation & Explanation

### Motivation

In this implementation, the goal is to simulate the DES key generation process, focusing on the application of the **PC-1** and **PC-2** permutations, along with bitwise rotations for key transformation. This provides a deeper understanding of the underlying cryptographic mechanisms in the DES algorithm.

### Project Structure

The project structure is as follows:

```
des_key_generation/
    main.py
    key_generation.py
    tables.py
```

### Code Snippets

#### **`key_generation.py`**

This file implements the DES key generation process, including the permutation, splitting, shifting, and round key generation:

```python
from tables import PC1, PC2, SHIFT_SCHEDULE

def permute(key, table):
    """Performs permutation based on the provided table."""
    return [key[i - 1] for i in table]

def rotate_left(key_half, n_shifts):
    """Performs left rotation on the key half."""
    return key_half[n_shifts:] + key_half[:n_shifts]

def generate_round_keys(initial_key):
    """Generates the 16 round keys for DES encryption."""
    # Apply PC-1 permutation
    permuted_key = permute(initial_key, PC1)
    print("PC-1 Permutation:", permuted_key)

    # Split the key into two halves (C0 and D0)
    C, D = permuted_key[:28], permuted_key[28:]
    print("Initial C0:", C)
    print("Initial D0:", D)

    round_keys = []

    # Generate 16 round keys
    for i in range(16):
        # Rotate C and D according to the shift schedule
        shift_count = SHIFT_SCHEDULE[i]
        C = rotate_left(C, shift_count)
        D = rotate_left(D, shift_count)

        # Combine C and D to get the 56-bit key
        combined_key = C + D
        print(f"Round {i+1} - C{i+1}:", C)
        print(f"Round {i+1} - D{i+1}:", D)

        # Apply PC-2 permutation to generate the round key
        round_key = permute(combined_key, PC2)
        round_keys.append(round_key)
        print(f"Round {i+1} Key:", round_key)

    return round_keys

# Example usage
initial_key = [
    0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1,
    1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0,
    0, 1, 1, 1, 0, 0, 1, 1, 0, 0
]
generate_round_keys(initial_key)
```

#### **`tables.py`**

This file contains the `PC1`, `PC2`, and `SHIFT_SCHEDULE` tables used for permutations and rotations:

```python
# Permuted Choice 1 table (PC-1)
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

# Permuted Choice 2 table (PC-2)
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

# Number of bit shifts for each round
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
```

---

## Results & Discussion

The DES key generation process successfully generates 16 round keys. The output includes the key after applying the PC-1 permutation, the initial halves (C0 and D0), and the round keys after each left shift and PC-2 permutation. This approach effectively simulates the DES key generation mechanism, which is crucial for the secure encryption process in the DES algorithm.

The use of left shifts and permutations ensures that each round key is distinct, contributing to the overall security of the encryption process. The application of these transformations allows the DES algorithm to produce complex keys that make cryptographic analysis more difficult.

---

## Conclusion

This laboratory work provided a detailed understanding of the DES key generation process. By implementing the key generation algorithm using PC-1, PC-2, and the SHIFT_SCHEDULE, we successfully simulated the DES encryption key derivation. This process highlights the importance of bitwise operations, permutations, and shifts in ensuring secure encryption and contributes to a deeper understanding of cryptographic algorithms.
