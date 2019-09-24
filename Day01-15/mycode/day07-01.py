# -*- coding:utf-8 -*-

"""
在屏幕上显示跑马灯文字
"""

import os
import time


def main():
	content = '广州欢迎你━(*｀∀´*)ノ亻!'
	while True:
		# 清理屏幕上的输出
		os.system('cls')
		print content
		time.sleep(0.2)
		content = content[1:] + content[0]


if __name__ == '__main__':
	main()
