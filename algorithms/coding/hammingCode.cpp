#include "string"
#include "cmath"
#include "sstream"

std::string hammingCodeEncode(const std::string &s) {
    uint16_t parity_bits_count = std::log2(s.size()) + 1;

    size_t str_ptr = 0;
    uint64_t parity_bits_val = 0;

    for (size_t i = 1; i < s.size() + 1 + parity_bits_count; ++i) {
        if ((i & (i - 1)) != 0 && s[str_ptr++] == '1') {  // if not power of 2 and s[i] == '1'
            parity_bits_val ^= i;
        }
    }

    std::stringstream ss;
    str_ptr = 0;
    for (size_t i = 1; i < s.size() + 1 + parity_bits_count; ++i) {
        if ((i & (i - 1)) == 0) {  // if power of 2
            ss << (((parity_bits_val & i) == i) ? '1' : '0');
        } else {
            ss << s[str_ptr++];
        }
    }

    return ss.str();
}

std::string hammingCodeDecode(const std::string &s) {
    std::stringstream ss;
    uint64_t parity_bits_val = 0;

    for (size_t i = 1; i < s.size() + 1; ++i) {
        if (s[i - 1] == '1') {
            parity_bits_val ^= i;
        }
    }

    for (size_t i = 1; i < s.size() + 1; ++i) {
        if ((i & (i - 1)) != 0) {  // if not power of 2
            char ch = s[i - 1];
            if (parity_bits_val == i) {  // if error occurred on this index
                ch = (ch == '1' ? '0' : '1');
            }
            ss << ch;
        }
    }

    return ss.str();
}
