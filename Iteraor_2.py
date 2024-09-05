class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.items = []
        self.index = 0

    def __iter__(self):
        self.items = attachment(self.list_of_lists, self.items)
        return self

    def __next__(self):
        if self.index == len(self.items):
            raise StopIteration
        self.index += 1
        return self.items[self.index-1]

def attachment(attachment_list, items): #перебираем элементы
    for n, item in enumerate(attachment_list):
        items = item_list(item, items)
    return items

def item_list(item, items): # проверяем из чего состоит элемент
    if isinstance(item, list):
        attachment(item, items)
    else:
        items = item_save(item, items)

    return items

def item_save(item, items): # сохраняем найденный элемент
    items.append(item)
    return items


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()