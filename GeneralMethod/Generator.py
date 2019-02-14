# def triangles():
#     a = [1]
#     while a:
#         yield a
#         if len(a) == 1:
#             a = [1, 1]
#         else:
#             a = [a[i] + a[i + 1] for i in range(len(a) - 1)]
#             a = [1] + a + [1]
#
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


#asynchronize generator
import asyncio
async def ticker(delay,to):
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

t = ticker(1000,5)
print(t)