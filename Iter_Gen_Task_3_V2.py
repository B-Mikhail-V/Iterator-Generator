nested_list = [
	['a', 'b', 'c', [1, 2, [33, 44, 55, ['r', 4, 'zz']]]],
	['d', 'e', [121, 232, 343, 'ttt',[999, 1010, None,[False]]], 'f', 'h', False],
	[1, 2, None, [111, 444, 'sss']],
]

class FlatIterator():

    def __init__(self, llist):
        self.llist = llist


    def __iter__(self):
        self.main_list_cursor = -1  # курсор основного списка
        # self.nested_list_cursor = -1  # курсор списка вложенного в основной список
        return self

    def __next__(self):
        # self.nested_list_cursor += 1
        # if self.nested_list_cursor == len(self.llist[self.main_list_cursor]):
        self.main_list_cursor += 1
            # self.nested_list_cursor = 0
        if self.main_list_cursor == len(self.llist):
            raise StopIteration
        return self.llist[self.main_list_cursor]

# flatlist = []
def print_elements(list_2, flatlist=[]):
    for item in FlatIterator(list_2):
        if isinstance(item, list):
            print_elements(item)
        else:
            flatlist.append(item)
    return flatlist


if __name__ == '__main__':

    print(print_elements(nested_list))


