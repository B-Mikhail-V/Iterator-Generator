nested_list = [
	['a', 'b', 'c', [1, 2, [33, 44, 55, ['r', 4, 'zz']]]],
	['d', 'e', [121, 232, 343, 'ttt',[999, 1010, None,[False]]], 'f', 'h', False],
	[1, 2, None, [111, 444, 'sss']],
]

def print_elements(list_input):
	for items in list_input:
		if isinstance(items, list):
			print_elements(items)
		else:
			print(items)


if __name__ == '__main__':
	print_elements(nested_list)