import pytest
import random

from algorithms.coding.hammingCode import (
    hamming_code_encode,
    hamming_code_decode,
    get_parity_bits_count,
)


@pytest.mark.parametrize(
    "msg_len, answer", [(4, 3), (1, 1), (15, 5), (120, 7), (26, 5), (57, 6), (247, 8)]
)
def test_get_parity_bits_count(msg_len, answer):
    assert get_parity_bits_count(msg_len) == answer


class TestHammingEncode:
    def test_empty(self):
        assert hamming_code_encode("") == ""

    @pytest.mark.parametrize(
        "string, answer",
        [
            ('1', '11'),
            ("1010", "1011010"),
            ("1001010110", "11110011010110"),
            ("011", "110011"),
            ("001011", "1001010011"),
        ],
    )
    def test_basics(self, string, answer):
        assert hamming_code_encode(string) == answer


class TestHammingDecode:
    def test_empty(self):
        assert hamming_code_encode("") == ""

    @pytest.mark.parametrize(
        "string, answer",
        [
            ("00", "0"),
            ("000", "0"),
            ("1011010", "1010"),
            ("11110111010110", "1001010110"),
            ("1001010011", "001011"),
        ],
    )
    def test_basics(self, string, answer):
        assert hamming_code_decode(string) == answer


def test_hamming_code_decode():
    symbols = ("1", "0")
    for _ in range(100):
        rand_str = "".join(
            random.choice(symbols) for _ in range(random.randint(1, 100))
        )
        encoded = hamming_code_encode(rand_str)
        decoded = hamming_code_decode(encoded)

        assert (
            decoded == rand_str
        ), f"orig: {rand_str}, encoded: {encoded}, decoded: {decoded}"
