import pytest
from algorithms.search.binary import lower_bound, upper_bound
from algorithms.search.linear import linear_search


TEST_SEQ = [0, 1, 2, 2, 3, 5, 9]


class TestLowerBound:
    @pytest.mark.parametrize("target, answer", [(3, 4), (2, 2), (6, 6), (0, 0), (9, 6)])
    def test_basics(self, target, answer):
        assert lower_bound(TEST_SEQ, target) == answer

    def test_one_element(self):
        assert lower_bound([5], 5) == 0


class TestUpperBound:
    @pytest.mark.parametrize("target, answer", [(3, 5), (2, 4), (6, 6), (0, 1)])
    def test_basics(self, target, answer):
        assert upper_bound(TEST_SEQ, target) == answer


class TestLinearSearch:
    @pytest.mark.parametrize("target, answer", [(3, 4), (2, 2), (0, 0), (9, 6)])
    def test_basics(self, target, answer):
        assert linear_search(TEST_SEQ, target) == answer

    def test_one_element(self):
        assert lower_bound([5], 5) == 0
