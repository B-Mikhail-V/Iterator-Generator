# ИТЕРАТОРЫ
# используем, когда нужно добавить итерацию к какому-то существующему классу
# когда нужна нестандартная логика итерации

# самый обычный цикл for
my_list = [1, 2, 3]
for el in my_list:
	print("list:", el)

# for работает потому, что вызывает метод __next__ у списка
my_iter = iter(my_list)
print("iterator:", next(my_iter))
print("iterator:", next(my_iter))
print("iterator:", next(my_iter))
# если вызвать next в четвертый раз - получим исключение StopIteration, потому что элементов в списке было всего три
# так и работает for - он останавливается по StopIteration
# print("iterator:", next(my_iter))

# эти методы можно вызывать и напрямую:
my_iter = my_list.__iter__()
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())

# создаем свой собственный класс-итератор
# для этого в нем обязательно должны быть реализованы два метода: __iter__, который делает из него итератор,
# и __next__, чтобы можно было двигаться по элементам
class MyRange:
	def __init__(self, start, end, step=1):
		self.start = start
		self.end = end
		self.step = step

	def __iter__(self):
		# self.cursor - это "указатель". для начала его нужно поставить ПЕРЕД первым элементом последовательности
		self.cursor = self.start - 1
		return self

	def __next__(self):
		self.cursor += self.step
		# особенности именно итератора: если достигли последнего элемента, выкидываем исключение StopIteration
		if self.cursor == self.end+1:
			raise StopIteration
		# если последнего элемента все еще не достигли, просто возвращаем очередной элемент последовательности
		return self.cursor

# наш класс работает в цикле for как обычный list или range
for el in MyRange(1, 3):
	print("MyRange:", el)

# кроме list больше никто не хранит все элементы последовательности сразу. range и MyRange генерируют их "на лету"
# поэтому они такие маленькие: range 48 байт, MyRange 32 байта. а вот list занимает 8040 байт...
print("range занимает:", range(1000).__sizeof__())
print("list занимает:", list(range(1000)).__sizeof__())
print("MyRange занимает:", MyRange(1, 10001).__sizeof__())

# еще раз тренируемся использовать итератор:
# делаем свой класс, который перебирает ссылки на статьи про python на сайте pythondigest.ru
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

		# регулярка для поиска нужных ссылок на статьи в html
		pattern = r"<a class=\"issue-item-title\" href=\"([\w.\/-;&=?:]+)\""
		# все ссылки попадут в список self.articles. вот по нему и будет ходить наш итератор
		self.articles = re.findall(pattern, text)
		self.cursor = -1
		return self

	def __next__(self):
		self.cursor += 1
		if self.cursor == len(self.articles):
			raise StopIteration
		return self.articles[self.cursor] # возвращаем следующую ссылку из списка ссылок

print("Проверяем наш класс, который выводит ссылки с pythondigest.ru")
for url in MyLinks("https://pythondigest.ru/"):
	print(url)

# ГЕНЕРАТОРЫ и yield
# генераторы позволяют создавать простые последовательности

# когда мы используем yield, он отдает следующий элемент последовательности. но без return
# исключения здесь тоже не используются
def my_range(start, end):
    while start < end:
        yield start
        start += 1

# а цикл for и здесь выглядит так же, как обычно
for i in my_range(1, 4):
	print("yield:", i)

# наша домашка про словари :) - возьмем из нее исходные данные
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def geoid(geoids):
	values = geoids.values() #[[213, 213, 213, 15, 213], [54, 54, 119, 119, 119], [213, 98, 98, 35]]
	for value in values: # на первом проходе будет [213, 213, 213, 15, 213]
		for el in value: # на первом проходе yield отдает 213, 213 и так далее
			yield el

# все значения выведутся в столбик
for id in geoid(ids):
	print(id)

# плоское представление - всего лишь конвертируем результат в list
ids_list = list(geoid(ids))
print(ids_list)

#генераторы и list comprehension
# стандартный алгоритм фильтрации целых чисел - мы все сделали вручную
test_list = list(range(10))
def my_filter(some_list):
	for el in some_list:
		if el % 2 == 0:
			yield el

print("yield с фильтром: ", list(my_filter(test_list)))

# list comprehension
# все то же самое, только код намного короче. на самом деле внутри тоже зашит for...
my_list = [x for x in range(10) if x%2==0]
print(my_list)