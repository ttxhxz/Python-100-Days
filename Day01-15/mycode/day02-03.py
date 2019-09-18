# -*- coding: utf-8 -*-
"""
输入年份 如果是闰年输出True 否则输出False
"""

year = int(input('请输入年份：'))
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
	print '{0}是闰年'.format(year)
else:
	print '{0}不是闰年'.format(year)
