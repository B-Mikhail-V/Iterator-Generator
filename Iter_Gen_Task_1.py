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

    def __str__(self):
        return "\n".join(str(element) for element in self.llist[self.cursor])


def print_el2(list_2):
    for item in FlatIterator(list_2):
        if isinstance(item, list):
            print_el(item)
        else:
            print(item)

def print_el(list_2):
    for item in FlatIterator(list_2):
        if isinstance(item, list):
            print_el(item)
        else:
            return item




if __name__ == '__main__':
    print(FlatIterator(nested_list))


    # print(FlatIterator(nested_list))

    # flat_list = [element for item in FlatIterator(nested_list) for element in FlatIterator(item)]
    # print(flat_list)
    #
    # flat_list = [element for item in FlatIterator(nested_list) for element in print_el(item)]
    # print(flat_list)