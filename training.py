# my_list = [1, 2, 3]
# for el in my_list:
#     print(el)
#
# my_iter = iter(my_list)
# print(type(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
#
#
# my_iter = my_list.__iter__()
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
#
# class MyRange:
#     def __init__(self, start, end, step=1):
#         self.start = start
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         self.cursor = self.start - 1
#         return self
#
#     def __next__(self):
#         self.cursor += self.step
#         if self.cursor == self.end:
#             raise StopIteration
#         return self.cursor
#
# for el in range(1, 4):
#     print("range", el)
#
# for el in MyRange(1, 4):
#     print("MyRange", el)
#
# print("range", range(1000).__sizeof__())
# print("range", list(range(1000)).__sizeof__())
# print("Myrange", range(1000).__sizeof__())

# Второй код
# import requests
# import re
#
# class MyLinks:
#     def __init__(self, url):
#         self.url = url
#
#     def __iter__(self):
#         text = requests.get(self.url).text
#         pattern = r"<a class=\"issue-item-title\" href=\"([\w.\/-;&=?:]+)\""
#         self.articles = re.findall(pattern, text)
#         self.cursor = -1
#         return self
#
#     def __next__(self):
#         self.cursor += 1
#         if self.cursor == len(self.articles):
#             raise StopIteration
#         return self.articles[self.cursor]
#
# for url in MyLinks("https://pythondigest.ru"):
#     print(url)


#
# def my_range(start, end, step):
#     while start < end:
#         yield start
#         start += step
#
# print(list(my_range(1, 4, 0.5)))

nested_list = [
	['a', 'b', 'c', [1, 2, [33, 44, 55, ['r', 4, 'zz']]]],
	['d', 'e', [121, 232, 343, 'ttt'], 'f', 'h', False],
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

# def print_items(list_1):
#     if isinstance(list_1, list):
#         FlatIterator(list_1)
#     else:
#         print_items(list_1)
#
#
# def pp(list_2):
#     for item in FlatIterator(list_2):
#         for el in FlatIterator(item):
#             print_items(el)
def make_el(list_2):
    for item1 in FlatIterator(list_2):
        if isinstance(item1, list):
            for el2 in FlatIterator(item1):
                if isinstance(el2, list):
                    return make_el(el2)
                else:
                    print(el2)
        print(item1)
    # print(list_2)

def print_fin(list_3):
    for items in FlatIterator(list_3):
        # print(items)
        if isinstance(items, list):
            for el2 in FlatIterator(items):
                if isinstance(el2, list):
                    print_fin(el2)
                else:
                    print(el2)
        else:
            print(items)

# def mmm(list_1):
#     if isinstance(make_el(list_1), list):
#         return make_el(list_1)
#     else:
#         print(make_el(list_1))

print_fin(nested_list)
