# The IP permutation matrix is used to permute the bits of the input block before further encryption.
# It sets the specific order of placing bits and affects the cryptographic stability of the algorithm.
# The IP matrix transforms the 64-bit block of data, placing the bits in a new order according to the specified positions.
# Each bit in the input position is moved to a new position, according to the values specified in the matrix.
initial_permutation = [57, 49, 41, 33, 25, 17, 9, 1,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5,
                       63, 55, 47, 39, 31, 23, 15, 7,
                       56, 48, 40, 32, 24, 16, 8, 0,
                       58, 50, 42, 34, 26, 18, 10, 2,
                       60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6
                       ]

# An expansion table is used to expand a 32-bit block of data to a 48-bit block before further encryption.
# It determines the specific order and placement of bits in the resulting block.
expansion_table = [
    31, 0, 1, 2, 3, 4,
    3, 4, 5, 6, 7, 8,
    7, 8, 9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0
]
# This table is called PC1 (Permutation Choice 1) and is used in the DES algorithm to permute the bits of the input 64-bit key before processing it further.
# PC1 defines the new order and placement of bits in the DES encryption/decryption key.
# The input key, which consists of 64 bits, is rearranged according to the specified positions in the PC1 table.
pc1 = [56, 48, 40, 32, 24, 16, 8,
       0, 57, 49, 41, 33, 25, 17,
       9, 1, 58, 50, 42, 34, 26,
       18, 10, 2, 59, 51, 43, 35,
       62, 54, 46, 38, 30, 22, 14,
       6, 61, 53, 45, 37, 29, 21,
       13, 5, 60, 52, 44, 36, 28,
       20, 12, 4, 27, 19, 11, 3
       ]

# The "left_rotations" table is used in the DES algorithm to perform cyclic left rotations for subkey generation.
# This table specifies the number of positions by which the bits of the left and right parts of the key must be shifted in each round of subkey generation.
# Each number in the table corresponds to a specific round and indicates how many positions the bits should be moved.

left_rotations = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

# The "pc2" table is used in the DES algorithm to generate subkeys.
# This table specifies which bits from the 56-bit key should be included in the 48-bit subkey for each round of the DES algorithm.

pc2 = [13, 16, 10, 23, 0, 4,
       2, 27, 14, 5, 20, 9,
       22, 18, 11, 3, 25, 7,
       15, 6, 26, 19, 12, 1,
       40, 51, 30, 36, 46, 54,
       29, 39, 50, 44, 32, 47,
       43, 48, 38, 55, 33, 52,
       45, 41, 49, 35, 28, 31
       ]

# After 16 rounds of DES encryption, the "fp" table is used to perform the last permutation of bits in the original ciphertext.
# This permutation is intended to protect the ciphertext from attacks using statistical analysis.

final_permutation = [
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
    32, 0, 40, 8, 48, 16, 56, 24
]

# The "sbox" table is used to implement irreversible substitution in DES and introduce the necessary confusion into the encryption process.
# Each of the eight Sbox tables contributes to bit swapping to improve the security of the cipher.

sbox = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]

# Table "p" in the DES (Data Encryption Standard) algorithm is a permutation of bits.
# It is used after the substitution function and before the next round of encryption.
# The "p" table contains 32 output positions, each of which corresponds to a specific input bit position.
# When applying the "p" table, the bits of the input block are placed in a new order according to the positions specified in the table.
p = [
    15, 6, 19, 20, 28, 11,
    27, 16, 0, 14, 22, 25,
    4, 17, 30, 9, 1, 7,
    23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10,
    3, 24
]


# The key_generation function generates subkeys for the DES encryption algorithm based on the input key.
# DES is a symmetric block cipher that uses a 64-bit key. The 64-bit input key is split into two halves, and a cycle of 16 subkeys is used.
# Each subkey is used in encryption rounds to shuffle and shuffle data bits.
def key_generation(key_64):
    subkeys = []
    key_64_p = [key_64[pc1[i]] for i in range(56)]

    c0 = key_64_p[0:28]
    d0 = key_64_p[28:56]

    # subkeys are shifted and new subkeys are formed based on the shifted values
    for j in range(0, 16):
        for i in range(left_rotations[j]):
            c1 = c0[1:] + c0[:1]
            d1 = d0[1:] + d0[:1]
            c0 = c1[:]
            d0 = d1[:]
        tab_pc2 = c1 + d1

        # res_pc2 is a reduced size subkey that will be used during the DES encryption process.
        res_pc2 = [tab_pc2[pc2[i]] for i in range(48)]

        subkeys.append(res_pc2)

    return subkeys


# The function f(R, K) performs these operations for each round of the DES algorithm,
# helping to ensure reliable data mixing and transformation, which increases the level of encryption security.

def f(R, K):
    # The function uses an expansion table to convert a 32-bit R block to a 48-bit R48 block.
    # This helps increase the number of bits in the block and expand its input data.
    R48 = list(range(48))
    for i in range(48):
        R48[i] = R[expansion_table[i]]

    # After expanding the R block, an XOR operation is performed between R48 and the subkey K.
    # This allows the bits of the R block to be combined with the bits of the subkey
    after_XOR = [R48[j] ^ K[j] for j in range(48)]

    # the R48 block passes through the S-blocks, which perform the necessary bit replacement according to the values of the S-block tables.
    # This is making irreversible changes to the data and ensuring the required level of mixing.
    after_sbox = []
    for j in range(8):
        Sixbits = after_XOR[(j * 6):(j + 1) * 6]
        bits_1_6 = int(str(Sixbits[0]) + str(Sixbits[5]), 2)
        bits_2_5 = int(str(Sixbits[1]) + str(Sixbits[2]) + str(Sixbits[3]) + str(Sixbits[4]), 2)
        found_int = sbox[j][bits_1_6 * 16 + bits_2_5]
        after_sbox += [int(i) for i in bin(found_int)[2:].zfill(4)]

    result = after_sbox[:]
    # result is permuted using the permutation table P. This helps to further shuffle the bits and ensure cryptographic stability.
    for i in range(32):
        result[i] = after_sbox[p[i]]

    return result


# The function performs the encryption process using the DES algorithm.
# It takes as input a 64-bit block of plaintext_64 and a 64-bit key key_64 and returns a 64-bit ciphertext.
def DES(plaintext_64, key_64):
    subkeys = key_generation(key_64)
    iptext = plaintext_64[:]

    # The input plaintext_64 is subjected to initial permutation using the initial_permutation table.
    # The result is divided into two halves - L (left half) and R (right half).
    for i in range(64):
        iptext[i] = plaintext_64[initial_permutation[i]]
    L = iptext[:32]
    R = iptext[32:64]

    # This part of the code performs the transformation of the right and left halves of the block of text on each round of DES encryption,
    # providing diffusion and obfuscation of the data to achieve cryptographic stability.

    for i in range(16):
        f_result = f(R, subkeys[i])
        C = R[:]
        R = [L[q] ^ f_result[q] for q in range(32)]
        L = C[:]

    res = R + L
    fptext = res[:]

    # After the last round, the combined R and L go through the reverse permutation using the final_permutation table. Encrypted text is obtained.
    for i in range(64):
        fptext[i] = res[final_permutation[i]]

    return fptext


# the DES_decrypt function uses a key and ciphertext to decrypt data using the DES algorithm.

def DES_decrypt(ciphertext, key_64):
    # Ciphertext values undergo an initial permutation using the initial_permutation table.
    initial_permut = [ciphertext[initial_permutation[i]] for i in range(64)]

    L = initial_permut[:32]
    R = initial_permut[32:64]
    subkeys = key_generation(key_64)

    # This piece of code performs a reverse pass through the DES rounds to decrypt the ciphertext.
    # At each iteration, values are exchanged between the left and right halves, and a round function is calculated to decrypt the data.

    for i in range(15, -1, -1):
        f_result = f(R, subkeys[i])
        C = R[:]
        R = [L[q] ^ f_result[q] for q in range(32)]
        L = C[:]

    res = R + L
    final_result = [res[final_permutation[i]] for i in range(64)]

    return final_result


# This function performs encryption by applying the cipher block cipher (CBC) encryption mode using DES.
def CBC_DES_ENC(IV, text, key_hexa):
    key_binary = [int(i, 2) for i in bin(int('0x' + key_hexa, 16))[2:].zfill(64)]

    binary_text_array = []

    # The input text is converted to binary format, where each character is converted to its ASCII code and presented as a binary_text_array list.
    # Each ASCII character is represented as a bit string 8 bits long.
    for i in text:
        binary_text_array += [int(i, 2) for i in bin(ord(i))[2:].zfill(8)]

    # The number of blocks into which the binary text is divided is calculated.
    block_number = len(binary_text_array) / 64
    last_block_size = len(binary_text_array) % 64
    init_vect = IV[:]
    cypher_text = []

    # This piece of code encrypts each block of text using CBC (Cipher Block Chaining) mode.
    for i in range(int(block_number)):
        block = binary_text_array[i * 64:(i + 1) * 64]
        XOR_res = [int(init_vect[j]) ^ block[j] for j in range(64)]
        cipher_block = DES(XOR_res, key_binary)
        cypher_text += cipher_block
        init_vect = cipher_block[:]

    # This fragment allows the last block of text that is not a full 64-bit block to be processed in CBC mode.
    if (last_block_size != 0):
        block_number = block_number + 1
        last_block = binary_text_array[-last_block_size:] + [0] * (64 - last_block_size)
        XOR_res = [init_vect[i] ^ last_block[i] for i in range(64)]
        cipher_block = DES(XOR_res, key_binary)
        cypher_text += cipher_block

    # This piece of code converts ciphertext represented as a list of bits (cypher_text) into a list of ASCII characters.
    cypher_text_ascii_string = [chr(int(
        str(cypher_text[i]) + str(cypher_text[i + 1]) + str(cypher_text[i + 2]) + str(cypher_text[i + 3]) + str(
            cypher_text[i + 4]) + str(cypher_text[i + 5]) + str(cypher_text[i + 6]) + str(cypher_text[i + 7]), 2)) for i
        in range(0, len(cypher_text) - 1, 8)]

    return cypher_text_ascii_string


# the CBC_DES_DEC function decrypts the ciphertext that was encrypted using the DES algorithm in CBC mode using the specified key and seed vector.

def CBC_DES_DEC(IV, cyphertext, key_hexa):
    key_binary = [int(i, 2) for i in bin(int('0x' + key_hexa, 16))[2:].zfill(64)]
    binary_ciphertext_array = []

    for i in cyphertext:
        binary_ciphertext_array += [int(i, 2) for i in bin(ord(i))[2:].zfill(8)]
    block_number = len(binary_ciphertext_array) / 64

    init_vect = IV[:]
    text = []

    # This piece of code decrypts each block of ciphertext using the DES algorithm and CBC mode,
    # applying an XOR operation between the decrypted block and the previous block of ciphertext (initial vector).
    # The decryption result of each block is added to the text variable, which will contain the entire decrypted text.
    for i in range(int(block_number)):
        block = binary_ciphertext_array[i * 64:(i + 1) * 64]
        text_block = DES_decrypt(block, key_binary)
        XOR_res = [int(init_vect[i]) ^ text_block[i] for i in range(64)]
        text += XOR_res
        init_vect = block[:]

    # converts a text list that contains the decoded text in binary format (0 and 1) to the corresponding decoded text as ASCII characters.
    text_ascii_string = [chr(int(
        str(text[i]) + str(text[i + 1]) + str(text[i + 2]) + str(text[i + 3]) + str(text[i + 4]) + str(
            text[i + 5]) + str(text[i + 6]) + str(text[i + 7]), 2)) for i in range(0, len(text) - 1, 8)]

    return text_ascii_string


# demonstrates an example of using the CBC_DES_ENC and CBC_DES_DEC functions to encrypt and decrypt text using DES in CBC mode.
def test():
    IV = [0] * 40 + [1] * 20 + [0] * 4

    text = "Cryptology course"
    KEY = "1f4f8a113b4a5d66"

    cypher_text = CBC_DES_ENC(IV, text, KEY)
    original_text = CBC_DES_DEC(IV, cypher_text, KEY)

    print("cypher_text", cypher_text)
    print("original_text", original_text)


test()