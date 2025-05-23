INITIAL_PERM_TABLE = [58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17, 9, 1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7]

FINAL_PERM_TABLE = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]

EXPAND_TABLE = [32, 1, 2, 3, 4, 5,
                4, 5, 6, 7, 8, 9,
                8, 9, 10, 11, 12, 13,
                12, 13, 14, 15, 16, 17,
                16, 17, 18, 19, 20, 21,
                20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,
                28, 29, 30, 31, 32, 1]

PERM_TABLE = [16, 7, 20, 21, 29, 12, 28, 17,
              1, 15, 23, 26, 5, 18, 31, 10,
              2, 8, 24, 14, 32, 27, 3, 9,
              19, 13, 30, 6, 22, 11, 4, 25]

SUBSTITUTION_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

KEY_PERM_1 = [57, 49, 41, 33, 25, 17, 9,
              1, 58, 50, 42, 34, 26, 18,
              10, 2, 59, 51, 43, 35, 27,
              19, 11, 3, 60, 52, 44, 36,
              63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
              14, 6, 61, 53, 45, 37, 29,
              21, 13, 5, 28, 20, 12, 4]

KEY_PERM_2 = [14, 17, 11, 24, 1, 5, 3, 28,
              15, 6, 21, 10, 23, 19, 12, 4,
              26, 8, 16, 7, 27, 20, 13, 2,
              41, 52, 31, 37, 47, 55, 30, 40,
              51, 45, 33, 48, 44, 49, 39, 56,
              34, 53, 46, 42, 50, 36, 29, 32]

ROTATION_AMOUNTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def text_to_binary_array(message):
    byte_data = message.encode('utf-8')
    bit_list = []
    for byte_val in byte_data:
        binary_rep = bin(byte_val)[2:].zfill(8)
        for digit in binary_rep:
            bit_list.append(int(digit))
    return bit_list

def binary_array_to_text(bit_sequence):
    byte_buffer = bytearray()
    for idx in range(0, len(bit_sequence), 8):
        byte_chunk = bit_sequence[idx:idx+8]
        if len(byte_chunk) == 8:
            byte_value = int(''.join([str(b) for b in byte_chunk]), 2)
            byte_buffer.append(byte_value)

    try:
        return byte_buffer.decode('utf-8')
    except UnicodeDecodeError:
        for i in range(len(byte_buffer), 0, -1):
            try:
                return byte_buffer[:i].decode('utf-8')
            except UnicodeDecodeError:
                continue
        return ""

def apply_permutation(data_block, perm_table):
    return [data_block[pos-1] for pos in perm_table]

def divide_block(block):
    mid_point = len(block)//2
    return block[:mid_point], block[mid_point:]

def bitwise_xor(first_bits, second_bits):
    return [first_bits[i] ^ second_bits[i] for i in range(len(first_bits))]

def circular_left_shift(block, shift_count):
    return block[shift_count:] + block[:shift_count]

def create_round_keys(master_key):
    key_bits = text_to_binary_array(master_key)

    if len(key_bits) < 64:
        key_bits = key_bits + [0] * (64 - len(key_bits))
    elif len(key_bits) > 64:
        key_bits = key_bits[:64]

    compressed_key = apply_permutation(key_bits, KEY_PERM_1)
    left_half, right_half = divide_block(compressed_key)

    round_keys = []
    for round_num in range(16):
        left_half = circular_left_shift(left_half, ROTATION_AMOUNTS[round_num])
        right_half = circular_left_shift(right_half, ROTATION_AMOUNTS[round_num])

        merged_halves = left_half + right_half
        round_key = apply_permutation(merged_halves, KEY_PERM_2)
        round_keys.append(round_key)

    return round_keys

def feistel_function(right_data, round_key):
    expanded_data = apply_permutation(right_data, EXPAND_TABLE)
    xored_data = bitwise_xor(expanded_data, round_key)

    sbox_result = []
    for box_index in range(8):
        six_bit_chunk = xored_data[box_index*6:(box_index+1)*6]
        row_index = int(str(six_bit_chunk[0]) + str(six_bit_chunk[5]), 2)
        col_index = int(''.join([str(bit) for bit in six_bit_chunk[1:5]]), 2)

        sbox_value = SUBSTITUTION_BOXES[box_index][row_index][col_index]
        four_bit_rep = bin(sbox_value)[2:].zfill(4)
        for bit_char in four_bit_rep:
            sbox_result.append(int(bit_char))

    return apply_permutation(sbox_result, PERM_TABLE)

def encrypt_single_block(data_block, round_keys):
    permuted_block = apply_permutation(data_block, INITIAL_PERM_TABLE)
    left_part, right_part = divide_block(permuted_block)

    for round_index in range(16):
        old_right = right_part
        feistel_output = feistel_function(right_part, round_keys[round_index])
        right_part = bitwise_xor(left_part, feistel_output)
        left_part = old_right

        if round_index == 0:
            print(f"Після 1-го раунду:")
            print(f"Ліва частина: {''.join([str(bit) for bit in left_part])}")
            print(f"Права частина: {''.join([str(bit) for bit in right_part])}")

    final_combined = right_part + left_part
    return apply_permutation(final_combined, FINAL_PERM_TABLE)

def des_encrypt_text(plaintext, encryption_key):
    round_keys = create_round_keys(encryption_key)
    text_bits = text_to_binary_array(plaintext)

    if len(text_bits) % 64 != 0:
        padding_needed = 64 - (len(text_bits) % 64)
        text_bits = text_bits + [0] * padding_needed

    encrypted_result = []
    for block_start in range(0, len(text_bits), 64):
        current_block = text_bits[block_start:block_start+64]
        encrypted_result.extend(encrypt_single_block(current_block, round_keys))

    return encrypted_result

def des_decrypt_text(ciphertext_bits, decryption_key):
    round_keys = create_round_keys(decryption_key)
    round_keys.reverse()

    decrypted_result = []
    for block_start in range(0, len(ciphertext_bits), 64):
        current_block = ciphertext_bits[block_start:block_start+64]
        decrypted_result.extend(encrypt_single_block(current_block, round_keys))

    while decrypted_result and decrypted_result[-1] == 0:
        decrypted_result.pop()

    return binary_array_to_text(decrypted_result)

def convert_bits_to_hex(bit_array):
    hex_string = ""
    for nibble_start in range(0, len(bit_array), 4):
        if nibble_start + 4 <= len(bit_array):
            nibble_bits = bit_array[nibble_start:nibble_start+4]
            hex_digit = hex(int(''.join([str(b) for b in nibble_bits]), 2))[2:]
            hex_string += hex_digit
    return hex_string

def run_des_demonstration():
    input_text = "Галькевич Петро Миколайович, група 12-341"
    secret_key = "secretky"

    print(f"Текст для шифрування: {input_text}")
    print(f"Ключ: {secret_key}")

    print("\nШифрування:")
    cipher_bits = des_encrypt_text(input_text, secret_key)
    print(f"Зашифрований текст (HEX): {convert_bits_to_hex(cipher_bits)}")

    print("\nДешифрування:")
    recovered_text = des_decrypt_text(cipher_bits, secret_key)
    print(f"Розшифрований текст: {recovered_text}")

    print("\nДетальний аналіз першого раунду:")
    input_bits = text_to_binary_array(input_text)
    if len(input_bits) < 64:
        input_bits = input_bits + [0] * (64 - len(input_bits))
    first_block = input_bits[:64]

    key_schedule = create_round_keys(secret_key)

    after_initial_perm = apply_permutation(first_block, INITIAL_PERM_TABLE)
    print(f"Після початкової перестановки (IP): {convert_bits_to_hex(after_initial_perm)}")

    l_part, r_part = divide_block(after_initial_perm)
    print(f"Ліва частина (L0): {convert_bits_to_hex(l_part)}")
    print(f"Права частина (R0): {convert_bits_to_hex(r_part)}")

    expanded_r = apply_permutation(r_part, EXPAND_TABLE)
    print(f"Розширена права частина (E(R0)): {convert_bits_to_hex(expanded_r)}")

    xor_with_key = bitwise_xor(expanded_r, key_schedule[0])
    print(f"Результат XOR з підключем K1: {convert_bits_to_hex(xor_with_key)}")

    sbox_output = []
    for s_index in range(8):
        six_bits = xor_with_key[s_index*6:(s_index+1)*6]
        row_val = int(str(six_bits[0]) + str(six_bits[5]), 2)
        col_val = int(''.join([str(bit) for bit in six_bits[1:5]]), 2)
        substituted_val = SUBSTITUTION_BOXES[s_index][row_val][col_val]
        four_bit_val = bin(substituted_val)[2:].zfill(4)
        for bit in four_bit_val:
            sbox_output.append(int(bit))
    print(f"Вихід S-блоків: {convert_bits_to_hex(sbox_output)}")

    p_output = apply_permutation(sbox_output, PERM_TABLE)
    print(f"Результат перестановки P: {convert_bits_to_hex(p_output)}")

    new_r_part = bitwise_xor(l_part, p_output)
    print(f"Нова права частина (R1): {convert_bits_to_hex(new_r_part)}")

    new_l_part = r_part
    print(f"Нова ліва частина (L1): {convert_bits_to_hex(new_l_part)}")

if __name__ == "__main__":
    run_des_demonstration()