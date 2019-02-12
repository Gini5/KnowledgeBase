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
      def __new__(cls, *args, **kwargs):
          if not hasattr(Singleton, "_instance"): # 反射
              Singleton._instance = object.__new__(cls)
          return Singleton._instance

a = Singleton()
print(id(a))
b = Singleton()
print(id(b))
c = Singleton()
print(id(b))