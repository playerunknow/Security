import random

def is_simple(val):
    if val <= 1:
        return False
    if val <= 3:
        return True
    if val % 2 == 0 or val % 3 == 0:
        return False
    step = 5
    while step * step <= val:
        if val % step == 0 or val % (step + 2) == 0:
            return False
        step += 6
    return True

def create_prime(bit_len):
    while True:
        number = random.getrandbits(bit_len)
        number |= 1
        if is_simple(number):
            return number

def calc_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def mod_inv(a, m):
    def ext_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, u, v = ext_gcd(b % a, a)
        return (g, v - (b // a) * u, u)

    g, inv, _ = ext_gcd(a, m)
    if g != 1:
        raise ValueError("No inverse exists")
    return inv % m

def gen_keys(size=8):
    prime1 = create_prime(size)
    prime2 = create_prime(size)
    while prime1 == prime2:
        prime2 = create_prime(size)

    modulus = prime1 * prime2
    phi_val = (prime1 - 1) * (prime2 - 1)

    pub_exp = random.randrange(2, phi_val)
    while calc_gcd(pub_exp, phi_val) != 1:
        pub_exp = random.randrange(2, phi_val)

    priv_exp = mod_inv(pub_exp, phi_val)

    return ((pub_exp, modulus), (priv_exp, modulus)), (prime1, prime2)

def rsa_encrypt(pub, msg):
    key_exp, mod_val = pub
    return [pow(ord(ch), key_exp, mod_val) for ch in msg]

def rsa_decrypt(priv, code):
    dec_exp, mod_val = priv
    return ''.join([chr(pow(num, dec_exp, mod_val)) for num in code])

def run():
    secret = " Галькевич Петро Миколайович, група 12-341"
    (pub_k, priv_k), (first_p, second_p) = gen_keys(8)

    print(f"RSA Key Generation:")
    print(f"Primes: {first_p}, {second_p}")
    print(f"n = {pub_k[1]}")
    print(f"φ(n) = {(first_p - 1) * (second_p - 1)}")
    print(f"Public key: {pub_k}")
    print(f"Private key: {priv_k}")

    enc = rsa_encrypt(pub_k, secret)
    print(f"\nOriginal message: {secret}")
    print(f"Encrypted (numbers): {enc}")

    dec = rsa_decrypt(priv_k, enc)
    print(f"Decrypted message: {dec}")

    print("\nDetailed RSA Steps:")
    print("-" * 60)
    print("| Char  | Code   | Enc (m^e mod n) | Encrypted | Dec (c^d mod n) |")
    print("-" * 60)

    e, mod_n = pub_k
    d, _ = priv_k

    for sym in secret:
        m_val = ord(sym)
        encrypted = pow(m_val, e, mod_n)
        decrypted = pow(encrypted, d, mod_n)
        print(f"| {sym:^6} | {m_val:^6} | {m_val}^{e} mod {mod_n} | {encrypted:^9} | {encrypted}^{d} mod {mod_n} = {decrypted:^5} |")

    print("-" * 60)

if __name__ == "__main__":
    run()
