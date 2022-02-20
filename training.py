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

def my_range(start, end, step):
    while start < end:
        yield start
        start += step

print(list(my_range(1, 4, 0.5)))
