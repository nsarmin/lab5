class Heap:

    def __init__(self):
        self.heap_array = [0]
        self.current_size = 0

    def insert(self, k):
        self.heap_array.append(k)
        self.current_size = self.current_size + 1
        self.move_item_up(self.current_size)

    # This method moves an item to the top until it is in a proper spot
    def move_item_up(self, i):
        while i // 2 > 0:
            if self.heap_array[i] < self.heap_array[i // 2]:  # i // 2 gets parent node
                temp = self.heap_array[i // 2]
                self.heap_array[i // 2] = self.heap_array[i]
                self.heap_array[i] = temp
            i = i // 2

    # This method moves an item to the bottom until it is in a proper spot
    def move_item_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self.min_child(i)
            if self.heap_array[i] > self.heap_array[min_child]:
                temp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[min_child]
                self.heap_array[min_child] = temp
            i = min_child

    # This method finds the smallest child
    def min_child(self, i):
        if i * 2 + 1 > self.current_size:  # stops when there isn't anything left
            return i * 2
        else:
            if self.heap_array[i * 2] < self.heap_array[i * 2 + 1]:  # compares amounts
                return i * 2
            else:
                return 1 * 2 + 1

    # This method returns the smallest item left in the array
    def get_min_child(self):
        value = self.heap_array[1]
        self.heap_array[1] = self.heap_array[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_array.pop()
        self.move_item_down(1)
        return value

    # This method builds the heap
    def build_heap(self, items):
        i = len(items) // 2
        self.current_size = len(items)
        self.heap_array = [0] + items[:]
        while i > 0:
            self.move_item_down(i)
            i = i - 1
