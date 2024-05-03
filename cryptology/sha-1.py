import sys
import struct


class SHA1:
    # The constructor initializes the initial values of registers H0-H4, which are used during the execution of the SHA-1 algorithm.
    # Registers H0-H4 are 32-bit variables that store the state of the hash function at a certain stage of its operation.
    def __init__(self):
        self.__H = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ]

    # The expression (hex(h)[2:]).rjust(8, '0') converts each value of h in the list self.__H to a hexadecimal string prefixed with 0x,
    # discards the prefix 0x, and then prepends the string to get a term of a fixed length of 8 characters.
    # As a result, when the __str__() method is called for an object of the SHA1 class,
    # a string containing a string representation of the values of registers H0-H4 in a format suitable for further use or display will be returned.

    def __str__(self):
        return ''.join((hex(h)[2:]).rjust(8, '0') for h in self.__H)

    # __ROTL() is used to perform a cyclic shift of the bits of the number x by n positions to the left (rotate left).
    # As a result of performing a cyclic shift, the bits of the number are moved to the left, and the displaced bits are moved to the right side.
    @staticmethod
    def __ROTL(n, x, w=32):
        return ((x << n) | (x >> w - n)) & ((1 << w) - 1)

    # The __padding() method in this code is a static method of the SHA1 class and is used to add padding to the input data before processing it in the SHA-1 algorithm.
    @staticmethod
    def __padding(stream):
        l = len(stream)  # Bytes
        # the value hl is calculated, which represents the length of the input data in bits and is multiplied by 8 (l * 8).
        # Then, this value is packed in '>Q' format using the struct.pack() function.
        #  The format '>Q' indicates the byte order (big-endian) and data type Q (unsigned long long - unsigned 64-bit integer).
        hl = struct.pack('>Q', l * 8)

        # n this code, the value of l0 is calculated, which is the number of zero bytes that must be added to the input data during padding before processing by the SHA-1 algorithm.
        l0 = (56 - l) % 64
        if not l0:
            l0 = 64

        # padding is a concatenation of the byte sequence of the beginning of the complement, zero bytes and the 8-byte sequence hl
        padding = b'\x80' + b'\x00' * (l0 - 1) + hl

        return stream + padding

    # the input data is prepared for processing by the SHA-1 algorithm. It breaks the input data into blocks of 64 bytes and converts each block into a list of 32-bit words.
    @staticmethod
    def __prepare(stream):
        M = []
        n_blocks = len(stream) // 64

        # iterates over blocks of input data, splits each block into 16 words, and converts each word to an integer.
        for i in range(n_blocks):  # 64 Bytes per Block
            m = []

            for j in range(16):  # 16 Words per Block
                # For each word in the block, a corresponding 4-byte slice is taken from the input stream and converted to an integer of type int.
                # The int.from_bytes() function takes two arguments: a slice of bytes and a byte order ('big' indicates big-endian byte order).
                n = int.from_bytes(stream[i * 64 + j * 4:i * 64 + j * 4 + 4], 'big')
                m.append(n)

            M.append(m[:])

        return M

    # This method is intended for debugging and allows you to monitor the values of intermediate variables during the execution of the SHA-1 algorithm.
    def __debug_print(self, t, a, b, c, d, e):
        print('t = {0} : \t'.format(t),
              (hex(a)[2:]).rjust(8, '0'),
              (hex(b)[2:]).rjust(8, '0'),
              (hex(c)[2:]).rjust(8, '0'),
              (hex(d)[2:]).rjust(8, '0'),
              (hex(e)[2:]).rjust(8, '0')
              )

    # the block data is converted using the intermediate values of the state variables.
    def __process_block(self, block):
        # the mask allows us to apply bitwise operations, such as bitwise AND (&), to ensure that the values of variables remain limited to 32 bits and do not go beyond this limit.
        MASK = 2 ** 32 - 1

        W = block[:]

        # the loop allows you to expand the list W to 80 elements, using the values from the previous elements and applying certain bitwise operations for each new element.
        for t in range(16, 80):
            W.append(self.__ROTL(1, (W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16])) & MASK)

        # after executing this line of code, the variables a, b, c, d and e will contain the values of the elements of the self.__H list,
        # and we can access these values individually for further calculations and manipulations.
        a, b, c, d, e = self.__H[:]

        # They perform transformations on the current state of the hash value (variables a, b, c, d, e)
        # and the message block (W[t]) to update the state of the hash value for the next block.
        for t in range(80):
            if t <= 19:
                K = 0x5A827999
                # The function f represents a non-linear transformation that combines the values b, c, and d. It uses the AND (&) and OR (^) operators to create a new value.
                # This transformation adds additional complexity and non-linearity to the hashing process, which contributes to the cryptographic strength of the algorithm.
                f = (b & c) ^ (~b & d)
            elif t <= 39:
                K = 0x6ED9EBA1
                f = b ^ c ^ d
            elif t <= 59:
                K = 0x8F1BBCDC
                f = (b & c) ^ (b & d) ^ (c & d)
            else:
                K = 0xCA62C1D6
                f = b ^ c ^ d

            # each iteration processes a block of data, updates the values of the state variables,
            # and moves on to the next iteration to process the next block of data.
            #  This process is repeated until all blocks of the message are processed in the SHA-1 algorithm.
            T = ((self.__ROTL(5, a) + f + e + K + W[t]) & MASK)
            e = d
            d = c
            c = self.__ROTL(30, b) & MASK
            b = a
            a = T

            # self.__debug_print(t, a, b, c, d, e)
        # These state variable update operations ensure that the hash values are correctly updated after each message block is processed in the SHA-1 algorithm.
        self.__H[0] = (a + self.__H[0]) & MASK
        self.__H[1] = (b + self.__H[1]) & MASK
        self.__H[2] = (c + self.__H[2]) & MASK
        self.__H[3] = (d + self.__H[3]) & MASK
        self.__H[4] = (e + self.__H[4]) & MASK

        # The update method is used to update the state of the SHA-1 hash function by processing the input.

    def update(self, data):
        # The input data type is checked. If the data is a string (str), then it is converted to a UTF-8 encoded byte string using the encode('utf-8') method.
        # This is done in order to ensure a consistent representation of the data as a sequence of bytes.
        if isinstance(data, str):
            data = data.encode('utf-8')

        # The padding is performed according to the rules of the SHA-1 algorithm to ensure that the data length is a multiple of 512 bits.
        stream = self.__padding(data)
        blocks = self.__prepare(stream)

        # the basic steps of the SHA-1 algorithm are performed to update the state of the hash function based on the block data.
        for block in blocks:
            self.__process_block(block)

    # The digest method is used to get the final hash value after all input has been processed.
    def digest(self):
        digest_bytes = b''
        for h in self.__H:
            digest_bytes += struct.pack('>I', h)
        return digest_bytes

    # the hexdigest method retrieves the final SHA-1 hash value as a string of hexadecimal characters.
    def hexdigest(self):
        return self.digest().hex()


def main():
    data = "Secret Message"
    # Creates an instance of a SHA1 object named h.

    h = SHA1()
    # Updates the hash value of the h object by calling the update method and passing it the string "Secret Message".

    h.update(data)
    # Obtains the final hexadecimal hash value by calling the hexdigest method of the h object and stores it in the hex_sha variable.

    hex_sha = h.hexdigest()

    # Prints the original string and hexadecimal hash value to the screen using the print function.
    print("str2hash: ", data)
    print(hex_sha)


main()
