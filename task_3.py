class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_flate = self.flatе(self.list_of_list)

    def flatе(self, lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(self.flatе(item))
            else:
                result.append(item)
        return result

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor < len(self.list_flate):
            r = self.list_flate[self.cursor]
            self.cursor += 1
            return r
        else:
            raise  StopIteration


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