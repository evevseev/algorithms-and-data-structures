#include <cstdlib>
#include <initializer_list>
#include <vector>

template <class ValueType>
class Heap {
    std::vector<ValueType> data_;

    size_t getLeftChildIndex(size_t parent) {
        return 2 * parent + 1;
    }
    size_t getRightChildIndex(size_t parent) {
        return 2 * parent + 2;
    }

    size_t getParentIndex(size_t child) {
        return (child - 1) / 2;
    }

    void swapElements(size_t idx1, size_t idx2) {
        ValueType temp_val = data_[idx1];
        data_[idx1] = data_[idx2];
        data_[idx2] = temp_val;
    }

    void heapifyUp(size_t idx) {
        while (idx > 0 && data_[getParentIndex(idx)] < data_[idx]) {
            swapElements(idx, getParentIndex(idx));
            idx = getParentIndex(idx);
        }
    }

    void heapifyDown(size_t idx) {
        size_t vec_size = data_.size();

        while (true) {
            size_t l_idx = getLeftChildIndex(idx);
            size_t r_idx = getRightChildIndex(idx);
            size_t largest_el_idx = idx;

            if (l_idx < vec_size && data_[idx] < data_[l_idx]) {
                largest_el_idx = l_idx;
            }

            if (r_idx < vec_size && data_[largest_el_idx] < data_[r_idx]) {
                largest_el_idx = r_idx;
            }

            if (idx != largest_el_idx) {
                ValueType t_less = data_[idx];
                data_[idx] = data_[largest_el_idx];
                data_[largest_el_idx] = t_less;

                idx = largest_el_idx;
            } else {
                break;
            }
        }
    }

public:
    Heap() : data_() {
    }

    template <class Iterator>
    Heap(Iterator begin, Iterator end) {
        while (begin != end) {
            insert(*begin);
            ++begin;
        }
    }

    Heap(std::initializer_list<ValueType> values) {
        for (auto &val : values) {
            insert(val);
        }
    }

    Heap(const Heap &other) : data_(other.data_) {
    }

    Heap &operator=(const Heap &other) {
        if (this == &other) {
            return *this;
        }

        data_ = other.data_;
        return *this;
    }

    Heap(Heap &&other) {
        data_ = std::move(other.data_);
    }

    Heap &operator=(Heap &&other) {
        if (this == &other) {
            return *this;
        }

        data_ = std::move(other.data_);
        return *this;
    }

    ~Heap() = default;

    size_t size() const {
        return data_.size();
    }

    bool empty() const {
        return data_.empty();
    }

    void insert(const ValueType &val) {
        data_.push_back(val);
        heapifyUp(data_.size() - 1);
    }

    ValueType extract() {
        // Assumes that list.size() > 0
        ValueType res = data_[0];
        swapElements(0, data_.size() - 1);
        data_.pop_back();
        heapifyDown(0);
        return res;
    }
};
