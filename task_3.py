class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.result = []
    
    def loop(self, listing):
        for item in listing:
            if isinstance(item, list):
                self.loop(item)
            else:
                self.result.append(item)
        return self.result

    def __iter__(self):
        self.count = -1
        self.items = self.loop(self.list_of_list)
        return self
    
    def __next__(self):
        self.count += 1
        if self.count == len(self.items):
            raise StopIteration
        return self.items[self.count]

            
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