# -*- coding:utf-8 -*-
# def foo():
# 	print("starting...")
# 	while True:
# 		res = yield 4
# 		print("res:", res)
#
#
# g = foo()
# print(next(g))
# print("*" * 20)
# print(next(g))

# import sys
#
# print sys.getsizeof([1, 2, 3, 4, 5])
# print sys.getsizeof((1, 2, 3, 4, 5))

scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典进行遍历(遍历的其实是键再通过键取对应的值)
for elem in scores:
    print('%s\t--->\t%d' % (elem, scores[elem]))
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(one=111, two=222)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)
