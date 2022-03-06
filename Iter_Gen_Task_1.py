nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
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


def print_elements(list_input):
    for items in FlatIterator(list_input):
        for elements in FlatIterator(items):
            print(elements)


if __name__ == '__main__':
    print_elements(nested_list)
    list_elements = [element for items in FlatIterator(nested_list) for element in FlatIterator(items)]
    print(list_elements)
