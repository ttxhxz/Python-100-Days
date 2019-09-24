# -*- coding:utf-8 -*-

"""
设计一个函数产生指定长度的验证码,验证码由大小写字母和数字构成.
"""
import random


def generate_code(code_len=4):
	"""
	生成指定长度的验证码
	
	:param code_len: 验证码长度
	:return: 由大小写英文字母和数字构成的随机验证码
	"""
	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	code = ""
	for _ in range(code_len):
		index = random.randint(0, all_chars.__len__() - 1)
		code += all_chars[index]
	return code


def main():
	code_len = int(raw_input('请输入你想要的验证码的长度:'))
	if code_len and code_len >= 0:
		print generate_code(code_len)
	else:
		print generate_code()
		pass


if __name__ == '__main__':
	main()
