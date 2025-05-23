def gronsfeld_transform(data, secret, is_decrypt=False):
    upper = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_"
    lower = upper.lower()
    length = len(data)
    full_key = ''.join(secret[i % len(secret)] for i in range(length))
    output = ''
    trace = []

    for idx, ch in enumerate(data):
        offset = int(full_key[idx])
        if is_decrypt:
            offset = -offset

        if ch in upper:
            pos = upper.index(ch)
            shifted = (pos + offset) % len(upper)
            output += upper[shifted]
            trace.append(f"{ch} → {upper[shifted]} ({pos}+{offset}={shifted})")
        elif ch in lower:
            pos = lower.index(ch)
            shifted = (pos + offset) % len(lower)
            output += lower[shifted]
            trace.append(f"{ch} → {lower[shifted]} ({pos}+{offset}={shifted})")
        else:
            output += ch
            trace.append(f"{ch} → (без змін)")

    return output, trace


# Демонстрація
message = "Галькевич Петро Миколайович, група 12-341"
passcode = "1845"

encoded, log_enc = gronsfeld_transform(message, passcode)
decoded, log_dec = gronsfeld_transform(encoded, passcode, is_decrypt=True)

print("Оригінал:", message)
print("Ключ:", passcode)
print("\nКроки шифрування:")
print('\n'.join(log_enc))
print("\nРезультат шифрування:", encoded)
print("\nКроки розшифрування:")
print('\n'.join(log_dec))
print("\nРезультат розшифрування:", decoded)
