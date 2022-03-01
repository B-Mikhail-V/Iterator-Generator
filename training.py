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
def my_range(start, end, step=1):
    while start < end:
        yield start
        start += step

# print(list(my_range(1, 4, 0.5)))

for el in my_range(1, 4):
    print("yield", el)


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def geoid(geoids):
    values = geoids.values()
    for value in values:
        for el in value:
            yield el

for id in geoid(ids):  # запись в колонку
    print(id)

ids_list = list(geoid(ids))  # плоская запись в одны строчку
print(ids_list)


# filter

num_list = list(range(10))
for el in num_list:
    if el % 2 == 0:
        print(el)

even = [x for x in list(range(10)) if x%2 == 0]
print(even)


# nested_list = [
# 	['a', 'b', 'c', [1, 2, [33, 44, 55, ['r', 4, 'zz']]]],
# 	['d', 'e', [121, 232, 343, 'ttt',[999, 1010, None,[False]]], 'f', 'h', False],
# 	[1, 2, None, [111, 444, 'sss']],
# ]
#
# class FlatIterator():
#
#     def __init__(self, llist):
#         self.llist = llist
#
#
#     def __iter__(self):
#         self.cursor = -1
#         return self
#
#     def __next__(self):
#         self.cursor += 1
#         if self.cursor == len(self.llist):
#             raise StopIteration
#         return self.llist[self.cursor]
#
# def make_el(list_2):
#     for item1 in FlatIterator(list_2):
#         if isinstance(item1, list):
#             for el2 in FlatIterator(item1):
#                 if isinstance(el2, list):
#                     return make_el(el2)
#                 else:
#                     print(el2)
#         print(item1)
#
# def print_fin(list_3):
#     for items in FlatIterator(list_3):
#         if isinstance(items, list):
#             for el2 in FlatIterator(items):
#                 if isinstance(el2, list):
#                     print_fin(el2)
#                 else:
#                     print(el2)
#         else:
#             print(items)
#
#
# print_fin(nested_list)
