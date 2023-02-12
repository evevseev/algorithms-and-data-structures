#include "iostream"
#include "vector"

size_t lastHeapIndex(std::vector<int> &vec) {
    if (vec.empty()) {
        return 0;
    }

    for (int i = 1; i < vec.size(); ++i) {
        size_t parent = (i - 1) / 2;
        if (vec[i] > vec[parent]) {
            return i - 1;
        }
    }
    
    return vec.size() - 1;
}