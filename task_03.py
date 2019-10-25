class Heap:
    def __init__(self, arr):
        self.arr = arr

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * (i + 1)

    def __len__(self):
        return len(self.arr)

    def add_val(self, value):
        self.arr.append(value)

    def __getitem__(self, item):
        return self.arr[item]


class MaxHeap(Heap):
    def __init__(self, arr):
        super().__init__(arr)
        self.build_max_heap()

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l < len(self) and self.arr[l] > self.arr[i]:
            largest = l
        else:
            largest = i
        if r < len(self) and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        size = len(self)
        for i in range(int(size / 2), -1, -1):
            self.max_heapify(i)

    def add_val(self, value):
        super().add_val(value)
        i = len(self) - 1
        while i >= 1 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[
                self.parent(i)]
            i = self.parent(i)

    def pop_root(self, item):
        res = self.arr[0]
        self.arr[0] = self.arr.pop(-1)
        self.max_heapify(item)
        return res


class MinHeap(Heap):
    def __init__(self, arr):
        super().__init__(arr)
        self.build_min_heap()

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l < len(self) and self.arr[l] < self.arr[i]:
            smallest = l
        else:
            smallest = i
        if r < len(self) and self.arr[r] < self.arr[smallest]:
            smallest = r
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)

    def build_min_heap(self):
        size = len(self)
        for i in range(int(size / 2), -1, -1):
            self.min_heapify(i)

    def add_val(self, value):
        super().add_val(value)
        i = len(self) - 1
        while i >= 1 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[
                self.parent(i)]
            i = self.parent(i)

    def pop_root(self, item):
        res = self.arr[0]
        self.arr[0] = self.arr.pop(-1)
        self.min_heapify(item)
        return res


class Median:
    def __init__(self):
        self.high = MinHeap([])
        self.low = MaxHeap([])

    def add_element(self, value):
        to_pop_from = None
        if not self.low or self.low[0] > value:
            if len(self.low) > len(self.high):
                to_pop_from = self.low
                to_pop_to = self.high
            self.low.add_val(value)
        else:
            if len(self.high) > len(self.low):
                to_pop_from = self.high
                to_pop_to = self.low
            self.high.add_val(value)

        if to_pop_from:
            to_pop_to.add_val(to_pop_from.pop_root(0))

    def get_median(self):
        low_len = len(self.low)
        high_len = len(self.high)
        even = (low_len + high_len) % 2 == 0
        if even:
            return self.low[0], self.high[0]
        if low_len < high_len:
            return self.high[0]
        return self.low[0]

    def get_maxheap_elements(self):
        return self.low.arr

    def get_minheap_elements(self):
        return self.high.arr


class PairingMedian(Median):
    def __init__(self):
        pass


if __name__ == '__main__':
    import random
    random.seed(10)

    test_nums = random.sample(range(100), 10)
    test_nums.reverse()
    m = Median()
    for el in test_nums:
        m.add_element(el)
        print(el)
        print(m.get_median())
        print('high max: ', m.get_minheap_elements())
        print('low max: ', m.get_maxheap_elements())
        print()
        print()
