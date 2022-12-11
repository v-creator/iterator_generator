from functools import reduce
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
    
    def red(list):
        return reduce(lambda x,y: x + y, list)

    def __iter__(self):
        self.count = -1
        self.exit = len(self.list_of_list)
        return self
    
    def __next__(self):
        for item in self.list_of_list:
            if any(isinstance(i, list) for i in item):
                print(item)
                item = self.red(item)
                print(item)
            


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
        pass
        # print(flat_iterator_item)
        # assert flat_iterator_item == check_item

    # assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()