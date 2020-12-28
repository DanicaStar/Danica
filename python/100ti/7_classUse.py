class Foo():
    def __init__(self):
        pass
    def __getattr__(self, item):
        print(item)
        return self

    def __str__(self):
        return ''
print(Foo().think.different.danica)