# константи алгоритма DES
IP_T = [58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]

IP_INV_T = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]

E_T = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
       8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
       16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
       24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

P_T = [16, 7, 20, 21, 29, 12, 28, 17,
       1, 15, 23, 26, 5, 18, 31, 10,
       2, 8, 24, 14, 32, 27, 3, 9,
       19, 13, 30, 6, 22, 11, 4, 25]

SBOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

PC1_T = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
         10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
         63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
         14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2_T = [14, 17, 11, 24, 1, 5, 3, 28,
         15, 6, 21, 10, 23, 19, 12, 4,
         26, 8, 16, 7, 27, 20, 13, 2,
         41, 52, 31, 37, 47, 55, 30, 40,
         51, 45, 33, 48, 44, 49, 39, 56,
         34, 53, 46, 42, 50, 36, 29, 32]

SHIFT_VALS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def to_bits(txt: str) -> list[int]:
    out = []
    for byte in txt.encode():
        out.extend(int(b) for b in f"{byte:08b}")
    return out


def bits_to_str(bits: list[int]) -> str:
    buf = bytearray()
    for i in range(0, len(bits), 8):
        chunk = bits[i:i + 8]
        if len(chunk) == 8:
            buf.append(int("".join(map(str, chunk)), 2))
    try:
        return buf.decode()
    except UnicodeDecodeError:
        for j in range(len(buf), 0, -1):
            try:
                return buf[:j].decode()
            except UnicodeDecodeError:
                continue
        return ""


def apply_perm(seq: list[int], tbl: list[int]) -> list[int]:
    return [seq[i - 1] for i in tbl]


def halves(seq: list[int]) -> tuple[list[int], list[int]]:
    mid = len(seq) // 2
    return seq[:mid], seq[mid:]


def xor_bits(a: list[int], b: list[int]) -> list[int]:
    return [x ^ y for x, y in zip(a, b)]


def rotl(seq: list[int], n: int) -> list[int]:
    return seq[n:] + seq[:n]


def build_round_keys(secret: str) -> list[list[int]]:
    key_bits = to_bits(secret)
    key_bits = (key_bits + [0] * 64)[:64]
    key56 = apply_perm(key_bits, PC1_T)
    c, d = halves(key56)
    rounds = []
    for shift in SHIFT_VALS:
        c, d = rotl(c, shift), rotl(d, shift)
        rounds.append(apply_perm(c + d, PC2_T))
    return rounds


def feistel_f(r: list[int], k: list[int]) -> list[int]:
    exp = apply_perm(r, E_T)
    x = xor_bits(exp, k)
    out = []
    for idx in range(8):
        block = x[idx * 6:(idx + 1) * 6]
        row = (block[0] << 1) | block[5]
        col = int("".join(map(str, block[1:5])), 2)
        val = SBOX[idx][row][col]
        out.extend(int(b) for b in f"{val:04b}")
    return apply_perm(out, P_T)


def enc_block(chunk: list[int], keys: list[list[int]]) -> list[int]:
    block = apply_perm(chunk, IP_T)
    l, r = halves(block)
    for i in range(16):
        l, r = r, xor_bits(l, feistel_f(r, keys[i]))
        if i == 0:
            print("После 1-го раунда:")
            print("L:", "".join(map(str, l)))
            print("R:", "".join(map(str, r)))
    return apply_perm(r + l, IP_INV_T)


def des_encrypt(text: str, secret: str) -> list[int]:
    sub = build_round_keys(secret)
    bits = to_bits(text)
    if len(bits) % 64:
        bits += [0] * (64 - len(bits) % 64)
    res = []
    for i in range(0, len(bits), 64):
        res.extend(enc_block(bits[i:i + 64], sub))
    return res


def des_decrypt(cipher: list[int], secret: str) -> str:
    sub = build_round_keys(secret)[::-1]
    res = []
    for i in range(0, len(cipher), 64):
        res.extend(enc_block(cipher[i:i + 64], sub))
    while res and res[-1] == 0:
        res.pop()
    return bits_to_str(res)


def bits_hex(bits: list[int]) -> str:
    return "".join(hex(int("".join(map(str, bits[i:i + 4])), 2))[2:]
                   for i in range(0, len(bits), 4) if i + 4 <= len(bits))


def demo():
    plain = "Галькевич Петро Миколайович, група 12-341"
    key = "secretky"
    print("Исходный текст:", plain)
    print("Ключ:", key)
    print("\nШифрование:")
    enc = des_encrypt(plain, key)
    print("HEX:", bits_hex(enc))
    print("\nДешифрование:")
    dec = des_decrypt(enc, key)
    print("Расшифрованный текст:", dec)

    print("\nДетальный анализ первого раунда:")
    block = to_bits(plain) + [0] * (64 - len(to_bits(plain)) % 64)
    block = block[:64]
    subkeys = build_round_keys(key)
    ip = apply_perm(block, IP_T)
    l0, r0 = halves(ip)
    print("IP:", bits_hex(ip))
    print("L0:", bits_hex(l0))
    print("R0:", bits_hex(r0))
    e_r0 = apply_perm(r0, E_T)
    print("E(R0):", bits_hex(e_r0))
    k1_xor = xor_bits(e_r0, subkeys[0])
    print("E(R0) ⊕ K1:", bits_hex(k1_xor))
    s_out = []
    for idx in range(8):
        part = k1_xor[idx * 6:(idx + 1) * 6]
        row = (part[0] << 1) | part[5]
        col = int("".join(map(str, part[1:5])), 2)
        val = SBOX[idx][row][col]
        s_out.extend(int(b) for b in f"{val:04b}")
    print("S-box:", bits_hex(s_out))
    p_res = apply_perm(s_out, P_T)
    print("P:", bits_hex(p_res))
    new_r = xor_bits(l0, p_res)
    print("R1:", bits_hex(new_r))
    print("L1:", bits_hex(r0))


if __name__ == "__main__":
    demo()
