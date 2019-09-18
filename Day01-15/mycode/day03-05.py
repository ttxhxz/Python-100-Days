# -*- coding:utf-8 -*-
"""
输入月收入和五险一金计算个人所得税
个税起征点
	2018年10月1日起，个税起征点提高至5000元，使用超额累进税率的计算方法如下：
	1、全月应纳税所得额=税前收入-5000元(起征点)-专项扣除(三险一金等)-专项附加扣除-依法确定的其它扣除
	2、缴税=全月应纳税所得额*税率-速算扣除数
	例：假设小王的工资收入为8000元，专项扣除(三险一金等)扣除1000元，没有专项附加扣除，那么他应纳个人所得税为：
		(8000-5000-1000)*3%-0=60(元)

个税计算公式
	个人所得税计算明细=(税前收入-5000元(起征点)-专项扣除(三险一金等)-专项附加扣除-依法确定的其它扣除)*适用税率-速算扣除数

个税缴费税率
	1、全月应纳税所得额不超过3000元：
		税率：3%;速算扣除数(元)：0
	2、全月应纳税所得额超过3000元至12000元：
		税率：10%;速算扣除数(元)：210
	3、全月应纳税所得额超过12000元至25000元：
		税率：20%;速算扣除数(元)：1410
	4、全月应纳税所得额超过25000元至35000元：
		税率：25%;速算扣除数(元)：2660
	5、全月应纳税所得额超过35000元至55000元：
		税率：30%;速算扣除数(元)：4410
	6、全月应纳税所得额超过55000元至80000元：
		税率：35%;速算扣除数(元)：7160
	7、全月应纳税所得额超过80000元:
		税率：45%;速算扣除数(元)：15160

Tips：为什么是三险一金呢？因为生育保险和工伤保险全部是由企业承担，个人不需要缴纳，因此个人不能在个人所得税税前扣除。
"""

totalIncome = 0  # 税前收入
taxExThr = 5000  # tax exemption threshold 起征点，目前为5000
threeInsOneGolds = 0  # 专项扣除(三险一金等)
speAddDed = 0  # Special additional deductions 专项附加扣除
otherDed = 0  # Other deductions 依法确定的其它扣除
taxRate = 0  # 适用税率
qCalcDed = 0  # quick calculation deduction 速算扣除数
taxIncome = 0  # taxable income 全月应纳税所得额
tax = 0  # tax 税
income = 0  # 到手工资

totalIncome = float(raw_input('收入总额:'))
threeInsOneGolds = float(raw_input('专项扣除(三险一金等):'))
# 全月应纳税所得额=税前收入-5000元(起征点)-专项扣除(三险一金等)-专项附加扣除-依法确定的其它扣除
taxIncome = totalIncome - taxExThr - threeInsOneGolds - speAddDed - otherDed
if taxIncome <= 3000:
	taxRate = 0.03
	qCalcDed = 0
elif taxIncome <= 12000:
	taxRate = 0.1
	qCalcDed = 210
elif taxIncome <= 25000:
	taxRate = 0.2
	qCalcDed = 1410
elif taxIncome <= 35000:
	taxRate = 0.25
	qCalcDed = 2660
elif taxIncome <= 55000:
	taxRate = 0.3
	qCalcDed = 4410
elif taxIncome <= 80000:
	taxRate = 0.35
	qCalcDed = 7160
else:
	taxRate = 0.45
	qCalcDed = 15160
# 缴税=全月应纳税所得额*税率-速算扣除数
tax = abs(taxIncome * taxRate - qCalcDed)
income = totalIncome - threeInsOneGolds - tax
print '本月应缴税：{0:.2f}'.format(tax)
print '本月到手工资：{0:.2f}'.format(income)
