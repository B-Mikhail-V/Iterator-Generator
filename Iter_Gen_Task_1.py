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


# def print_elements(list_for_work):
#     for item in FlatIterator(list_for_work):
#         for element in FlatIterator(item):
#             print(element)

def print_el(list_2):
    FlatIterator(nested_list



if __name__ == '__main__':
    print_elements(nested_list)

    # print(FlatIterator(nested_list))

    flat_list = [element for item in FlatIterator(nested_list) for element in FlatIterator(item)]
    print(flat_list)
