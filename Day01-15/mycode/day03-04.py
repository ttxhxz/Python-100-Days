# -*- coding:utf-8 -*-
"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
海伦公式:   a,b,c三条边    p = (a+b+c)/2  面积s为 根号(p*(p-a)*(p-b)*(p-c))
"""
import math

a = float(raw_input('a = '))
b = float(raw_input('b = '))
c = float(raw_input('c = '))
if a + b > c and a + c > b and b + c > a:
	print '周长为: {0:.2f}'.format(a + b + c)
	p = (a + b + c) / 2
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print '面积为: {0:.2f}'.format(area)
else:
	print '不能构成三角形'
