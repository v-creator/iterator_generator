import types

def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list) and len(item)>1:
            yield from flat_generator(item)
        elif isinstance(item, bool | int | None):
            yield item
        elif isinstance(item, list) and len(item) == 1:
            for i_item in flat_generator(item):
                yield i_item
        else:
            yield from item
    

def test_4():
    
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
