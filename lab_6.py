def encrypt_by_dual_swap(message, key_x, key_y):
    length_x = len(key_x)
    length_y = len(key_y)
    block_size = length_x * length_y

    if len(message) < block_size:
        message += ' ' * (block_size - len(message))
    elif len(message) > block_size:
        return ''.join([
            encrypt_by_dual_swap(message[i:i + block_size], key_x, key_y)
            for i in range(0, len(message), block_size)
        ])

    grid = []
    for r in range(length_y):
        row_part = message[r * length_x:(r + 1) * length_x]
        grid.append(list(row_part))

    column_rearranged = [[''] * length_x for _ in range(length_y)]
    for r in range(length_y):
        for c, pos in enumerate(key_x):
            column_rearranged[r][c] = grid[r][int(pos) - 1]

    row_rearranged = [[''] * length_x for _ in range(length_y)]
    for r, pos in enumerate(key_y):
        for c in range(length_x):
            row_rearranged[r][c] = column_rearranged[int(pos) - 1][c]

    encrypted = ''
    for r in range(length_y):
        for c in range(length_x):
            encrypted += row_rearranged[r][c]

    return encrypted


def decrypt_by_dual_swap(ciphertext, key_x, key_y):
    columns = len(key_x)
    rows = len(key_y)
    block = columns * rows

    if len(ciphertext) > block:
        return ''.join([
            decrypt_by_dual_swap(ciphertext[i:i + block], key_x, key_y)
            for i in range(0, len(ciphertext), block)
        ])

    matrix = []
    for r in range(rows):
        segment = ciphertext[r * columns:(r + 1) * columns]
        matrix.append(list(segment))

    row_sorted = [[''] * columns for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            row_sorted[int(key_y[r]) - 1][c] = matrix[r][c]

    original_order = [[''] * columns for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            original_order[r][int(key_x[c]) - 1] = row_sorted[r][c]

    decrypted = ''
    for r in range(rows):
        for c in range(columns):
            decrypted += original_order[r][c]

    return decrypted.rstrip()


if __name__ == "__main__":
    original_message = "Галькевич Петро Миколайович, група 12-341"
    column_pattern = "2413"
    row_pattern = "4123"

    encrypted_result = encrypt_by_dual_swap(original_message, column_pattern, row_pattern)
    print("Зашифрований текст:", encrypted_result)

    decrypted_result = decrypt_by_dual_swap(encrypted_result, column_pattern, row_pattern)
    print("Розшифрований текст:", decrypted_result)
