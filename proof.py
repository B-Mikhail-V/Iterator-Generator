nested_list = [
    ['a', 'b', 'c', [11, 22, 33]],
    ['d', 'e', 'f'],
    [1, 2, None],
]

class Nested_iter:
    def __init__(self,nested_list):
        self.start = -1
        if len(nested_list):
            self.end = len(nested_list)
        else:
            self.end = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self

    def __str__(self):
        return '\n'.join(str(elem) for elem in nested_list[self.start])


if __name__ == '__main__':
    for elem in Nested_iter(nested_list):
        print(elem)

    lll = [elem for item in Nested_iter(nested_list) for elem in Nested_iter(item)]
    print(lll)