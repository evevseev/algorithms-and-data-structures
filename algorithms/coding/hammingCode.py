from math import log2, ceil


def get_parity_bits_count(msg_len: int) -> int:
    if msg_len == 1:
        return 1

    p = int(log2(msg_len + 1))

    while 2**p < msg_len + p + 1:
        p += 1

    return p


def hamming_code_encode(s: str) -> str:
    if not s:
        return ""

    parity_bits_count = get_parity_bits_count(len(s))
    str_ptr = 0
    parity_bits_val = 0

    for i in range(1, len(s) + 1 + parity_bits_count):
        if (i & (i - 1)) != 0:
            if s[str_ptr] == "1":  # if not power of 2 and s[i] == '1'
                parity_bits_val ^= i
            str_ptr += 1

    res: list[str] = []
    str_ptr = 0
    for i in range(1, len(s) + 1 + parity_bits_count):
        if (i & (i - 1)) == 0:  # if power of 2
            res.append("1" if ((parity_bits_val & i) == i) else "0")
        else:
            res.append(s[str_ptr])
            str_ptr += 1

    return "".join(res)


def hamming_code_decode(s: str) -> str:
    if len(s) == 2:
        if s[0] == s[1]:
            return s[1]
        else:
            return "0" if (s[1] == "1") else "1"

    res: list[str] = []
    parity_bits_val = 0

    for i in range(1, len(s) + 1):
        if s[i - 1] == "1":
            parity_bits_val ^= i

    for i in range(1, len(s) + 1):
        if (i & (i - 1)) != 0:  # if not power of 2
            ch = s[i - 1]
            if parity_bits_val == i:  # if error occurred on this index
                ch = "0" if (ch == "1") else "1"
            res.append(ch)
    return "".join(res)
