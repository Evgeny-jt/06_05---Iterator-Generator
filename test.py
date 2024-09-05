class FlatIterator:

    def __init__(self, list_of_list):
        print('init')
        self.list_of_lists = list_of_list
        self.items = []
        self.index = 0

    def __iter__(self):
        print('iter НАЧАЛО -хххххххххххххххххххххххххххххххххххх-')
        self.items = attachment(self.list_of_lists, self.items)
        print('-xxx-', self.items)
        print('iter ВЫХОД', self.items)
        print('ХХХХХХХХХХХХХХХХХХХХХХ  ВыХОД   ХХХХХХХХХХХХХХХХ')

        return self

    def __next__(self):
        print('NEXT', self.items)
        if self.index == len(self.items):
            raise StopIteration
        self.index += 1
        return self.items[self.index-1]

def attachment(attachment_list, items):
    print('f-', attachment_list)
    for n, item in enumerate(attachment_list):
        print('---------------------------------------------------------')
        print('f-итерация № ', n, 'элемент:', item, 'в списке-', items)
        items = item_list(item, items)
        print('-итерация', n, 'завершена. Полученый списоек:', items)
    print('-ВЫХОД', items, '============================================')
    return items

def item_list(item, items):
    print('f--item_list', item, 'спис', items)
    if isinstance(item, list):
        print('--это список: ', item)
        attachment(item, items)
    else:
        print('--это значение запишим его: ', item, 'в ', items)
        items = item_save(item, items)
        print('--Значение записанно', items, 'передаем его')

    return items

def item_save(item, items):
    print('f---item_save', item, '-', items)
    items.append(item)
    print('---', items)
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