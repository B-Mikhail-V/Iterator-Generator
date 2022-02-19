# my_list = [1, 2, 3]
# for el in my_list:
#     print("list:", el)
#
# my_iter = iter(my_list)
# print(type(my_iter))
# print("iterator:", next(my_iter))
# print("iterator:", next(my_iter))
# print("iterator:", next(my_iter))
# # print("iterator:", next(my_iter))
#
# my_iter = my_list.__iter__()
# print("iterator:", next(my_iter))
# print("iterator:", my_iter.__next__())
#
# my_tuple = (1, 2, 3)
# print(type(iter(my_tuple)))
#
my_dict = {"el1":1, "el2":2}
print(type(iter(my_dict)))
# print(type(iter(my_dict.values())))
#
class MyRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor+= self.step
        if self.cursor == self.end:
            raise StopIteration
        return self.cursor

for el in range(1, 4):
    print("range:", el)
#
# for el in MyRange(1, 4):
#     print("MyRange:", el)
#
# print("range занимает:", range(1000).__sizeof__())
# print("list занимает:", list(range(1000)).__sizeof__())
# print("MyRange занимает:", MyRange(1, 1001).__sizeof__())

import requests
import re

class MyLinks:
    def __init__(self, url):
        self.url = url

    def __iter__(self):
        text = requests.get(self.url).text

        # вот  так выглядят все нужные нам ссылки:
        # <a class="issue-item-title" href="https://habr.com/ru/post/650273/?utm_campaign=650273&amp;\
        # utm_source=habrahabr&amp;utm_medium=rss" onclick="trackUrl(59301, 'Статьи', 'Without tag');\
        # " rel="nofollow" target="_blank">Как перестать жить и начать беспокоится о потреблении памяти</a>

        pattern = r"<a class=\"issue-item-title\" href=\"([\w.\/-;&=?:]+)\""
        self.articles = re.findall(pattern, text)
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.articles):
            raise StopIteration
        return self.articles[self.cursor]

# for url in MyLinks("https://pythondigest.ru"):
#     print(url)

def my_range(start, end, step=1):
    while start < end:
        yield start
        start += step

for el in my_range(1, 4):
    print("yield:", el)

print("Функция my_range занимает", my_range.__sizeof__())

# наша домашка про словари :)
ids = {'user1': [213, 213, 213, [15], 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def geoid(geoids):
    values = geoids.values() #[[213, 213, 213, 15, 213], [54, 54, 119, 119, 119], [213, 98, 98, 35]]
    for value in values:
        for el in value:
            yield el

# ==================
# вот так делать не надо!
# def geoid(geoids):
#     values = geoids.values() #[[213, 213, 213, 15, 213], [54, 54, 119, 119, 119], [213, 98, 98, 35]]
#     for value in values:
#         for el in value:
#             return el
#
# print("Эксперимент")
# for id in geoid(ids):
#     print(id)
# # ==================


ids_list = list(geoid(ids))
print(ids_list)

num_list = list(range(10))
for el in num_list:
    if el % 2 == 0:
        print(el)

even = [x for x in list(range(10)) if x%2 == 0]
print(even)
