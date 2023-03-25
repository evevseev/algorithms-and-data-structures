class Heap:
    def __init__(self) -> None:
        self._data: list[int] = []

    @staticmethod
    def _get_left_child_index(parent: int) -> int:
        return 2 * parent + 1

    @staticmethod
    def _get_right_child_index(parent: int) -> int:
        return 2 * parent + 2

    @staticmethod
    def _get_parent_index(child: int) -> int:
        return (child - 1) // 2

    def _swap_elements(self, idx1: int, idx2: int) -> None:
        temp_val = self._data[idx1]
        self._data[idx1] = self._data[idx2]
        self._data[idx2] = temp_val

    def _heapify_up(self, idx: int) -> None:
        while idx > 0 and self._data[self._get_parent_index(idx)] < self._data[idx]:
            self._swap_elements(idx, self._get_parent_index(idx))
            idx = self._get_parent_index(idx)

    def _heapify_down(self, idx: int) -> None:
        data_size = len(self._data)
        while True:
            l_idx = self._get_left_child_index(idx)
            r_idx = self._get_right_child_index(idx)
            largest_el_idx = idx

            if l_idx < data_size and self._data[idx] < self._data[l_idx]:
                largest_el_idx = l_idx

            if r_idx < data_size and self._data[largest_el_idx] < self._data[r_idx]:
                largest_el_idx = l_idx

            if idx != largest_el_idx:
                t_less = self._data[idx]
                self._data[idx] = self._data[largest_el_idx]
                self._data[largest_el_idx] = t_less

                idx = largest_el_idx
            else:
                break

    def __len__(self) -> int:
        return len(self._data)

    def insert(self, val: int) -> None:
        self._data.append(val)
        self._heapify_up(len(self._data) - 1)

    def extract(self) -> int:
        res = self._data[0]
        self._swap_elements(0, len(self._data) - 1)
        self._data.pop()
        self._heapify_down(0)
        return res
