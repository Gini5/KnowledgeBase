#The singleton pattern is used to ensure one and only one object from a class gets created.
# class Singleton(object):
#     __instance = None
#
#     def __init__(self):
#         if not Singleton.__instance:
#             print('Instance does not exist')
#         else:
#             print('Instance exists:', self.get_instance())
#
#     @classmethod
#     def get_instance(cls):
#         if not cls.__instance:
#             cls.__instance = Singleton()
#         return cls.__instance

class Singleton(object):
    _singletons = {}
    def __new__(cls):
        if not cls._singletons.keys():            #若还没有任何实例
            cls._singletons[cls] = object.__new__(cls)  #生成一个实例
        return cls._singletons[cls]

a = Singleton()
print(id(a))
b = Singleton()
print(id(b))
c = Singleton()
print(id(b))