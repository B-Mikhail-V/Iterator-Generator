nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

def print_elements(list_input):
	for items in list_input:
		for element in items:
			yield element


if __name__ == '__main__':
	elements_list = [elements for elements in print_elements(nested_list)]
	print(elements_list)
	print(*print_elements(nested_list))

