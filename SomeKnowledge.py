'''
Different between classmethod and staticmethod
self: means the instance itself
cls: means the class itself, can use cls() to create an instance
'''
class A():
    a = 1

    @staticmethod
    def foo():
        print(A.a)
        # A.foo3("from foo")    cannot be use

    @classmethod
    def foo2(cls):
        print(cls.a)
        cls().foo3("from foo2")

    def foo3(self,v):
        print(v)

A.foo()
A.foo2()