class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.item = []

    def __iter__(self):
        self.index = 0
        self.items = []
        for list_ in self.list_of_lists:
            for item in list_:
                self.items.append(item)
        return self

    def __next__(self):

        if self.index == len(self.items):
            raise StopIteration
        self.index += 1
        return self.items[self.index-1]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
