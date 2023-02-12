#include <cstdlib>
#include <iostream>
#include <vector>

template <class T>
void heapify(std::vector<T> &vec, size_t idx, size_t size = 0) {
    size_t vec_size;
    if (size == 0) {
        vec_size = vec.size();
    } else {
        if (idx > vec_size) {
            return;
        }
        vec_size = size;
    }

    
    while (true) {
        size_t l_idx = 2 * idx + 1;
        size_t r_idx = 2 * idx + 2;
        size_t largest_el_idx = idx;

        if (l_idx < vec_size && vec[idx] < vec[l_idx]) {
            largest_el_idx = l_idx;
        }

        if (r_idx < vec_size && vec[largest_el_idx] < vec[r_idx]) {
            largest_el_idx = r_idx;
        }

        if (idx != largest_el_idx) {
            T t_less = vec[idx];
            vec[idx] = vec[largest_el_idx];
            vec[largest_el_idx] = t_less;

            idx = largest_el_idx;
        } else {
            break;
        }
    }
}

template <class T>
void heapSort(std::vector<T> &vec) {
    if (vec.empty()) {
        return;
    }

    size_t vec_size = vec.size();
    for (size_t i = vec_size / 2 + 1; i > 0; --i) {
        heapify(vec, i - 1);
    }

    size_t heap_size = vec.size();
    for (size_t i = 0; i + 1 < vec_size; ++i) {
        T tmp_max = vec[0];
        vec[0] = vec[vec_size - i - 1];
        vec[vec_size - i - 1] = tmp_max;

        heapify(vec, 0, --heap_size);
    }
}
