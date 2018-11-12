


class A:

    def __init__(self):
        print('init A')

    def a(self):
        print('A')

class B:

    def __init__(self):
        print('init B')

    def b(self):
        print('B')

d = {'a':A, 'b':B}


print(d['a']())

