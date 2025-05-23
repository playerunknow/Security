def encrypt_with_double_transposition(msg, key_col, key_row):
    kx = len(key_col)
    ky = len(key_row)
    total = kx * ky

    if len(msg) < total:
        msg += ' ' * (total - len(msg))
    elif len(msg) > total:
        return ''.join([encrypt_with_double_transposition(msg[i:i + total], key_col, key_row)
                        for i in range(0, len(msg), total)])

    matrix = []
    for y in range(ky):
        segment = msg[y * kx:(y + 1) * kx]
        matrix.append(list(segment))

    col_swapped = [[''] * kx for _ in range(ky)]
    for y in range(ky):
        for x, idx in enumerate(key_col):
            col_swapped[y][x] = matrix[y][int(idx) - 1]

    row_swapped = [[''] * kx for _ in range(ky)]
    for y, idx in enumerate(key_row):
        for x in range(kx):
            row_swapped[y][x] = col_swapped[int(idx) - 1][x]

    result = ''
    for y in range(ky):
        for x in range(kx):
            result += row_swapped[y][x]

    return result


def decrypt_with_double_transposition(cipher, key_col, key_row):
    w = len(key_col)
    h = len(key_row)
    block = w * h

    if len(cipher) > block:
        return ''.join([decrypt_with_double_transposition(cipher[i:i + block], key_col, key_row)
                        for i in range(0, len(cipher), block)])

    filled = []
    for y in range(h):
        line = cipher[y * w:(y + 1) * w]
        filled.append(list(line))

    row_restored = [[''] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            row_restored[int(key_row[y]) - 1][x] = filled[y][x]

    col_restored = [[''] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            col_restored[y][int(key_col[x]) - 1] = row_restored[y][x]

    plain = ''
    for y in range(h):
        for x in range(w):
            plain += col_restored[y][x]

    return plain.rstrip()


if __name__ == "__main__":
    original = "Галькевич Петро Миколайович, група 12-341"
    col_code = "2913"
    row_code = "4193"

    cipher = encrypt_with_double_transposition(original, col_code, row_code)
    print("Encrypted:", cipher)

    deciphered = decrypt_with_double_transposition(cipher, col_code, row_code)
    print("Decrypted:", deciphered)
