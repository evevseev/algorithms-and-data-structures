import pytest
from data_structures.binary_heap.binaryHeap import Heap
from random import randint


def test_empty_len():
    heap = Heap()
    assert len(heap) == 0


def test_empty_extraction():
    heap = Heap()
    with pytest.raises(Exception):
        heap.extract()


def test_element_addition():
    heap = Heap()
    for i in range(10):
        heap.insert(i)
        assert len(heap) == i + 1


def test_heap_invariant():
    heap = Heap()

    heap.insert(5)
    heap.insert(-5)
    heap.insert(34)

    assert heap.extract() == 34
    assert len(heap) == 2

    heap.insert(9)
    heap.insert(7)

    assert len(heap) == 4
    assert heap.extract() == 9
    assert heap.extract() == 7
    assert heap.extract() == 5
    assert heap.extract() == -5
    assert len(heap) == 0


def test_heap_invariant_under_stress():
    heap = Heap()

    for _ in range(10):
        data = {randint(-100, 100) for i in range(randint(1, 10))}

        for val in data:
            heap.insert(val)

        for _ in range(len(data)):
            val = heap.extract()
            assert val in data
            data.remove(val)
