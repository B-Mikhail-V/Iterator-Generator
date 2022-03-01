nested_list = [
	['a', 'b', 'c', [1, 2, [33, 44, 55, ['r', 4, 'zz']]]],
	['d', 'e', [121, 232, 343, 'ttt',[999, 1010, None,[False]]], 'f', 'h', False],
	[1, 2, None, [111, 444, 'sss']],
]

class FlatIterator():

    def __init__(self, llist):
        self.llist = llist


    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.llist):
            raise StopIteration
        return self.llist[self.cursor]


def print_all(list_3):
    for items in FlatIterator(list_3):
        if isinstance(items, list):
            for el2 in FlatIterator(items):
                if isinstance(el2, list):
                    print_all(el2)
                else:
                    print(el2)
        else:
            print(items)




if __name__ == '__main__':
    print_all(nested_list)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
