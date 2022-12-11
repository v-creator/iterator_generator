import logging

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

result = []

def flat_generator(list_o):
    _LOGGER.info(list_o)
    for item in list_o:
        if isinstance(item, list) and len(item) != 0:
            flat_generator(item)
        else:
            result.append(item)
    return result.pop(0)




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
        print(flat_iterator_item)
        # print(check_item)

        # assert flat_iterator_item == check_item

    # print(list(flat_generator(list_of_lists_2)))
    # assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    # assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    # print((flat_generator(list_of_lists_2)))
    test_4()
