#!/usr/bin/env python
# --*-- coding:utf-8 --*--

"""
# if 判断1
age = 3
if age >= 18:
    print('you age is',age)
    print('adult')
else:
    print('you age is',age)
    print('teenager')

#if判断2: birthday int
birth = input("birth:")
birth1 = int(birth)
if birth1 < 2000:
    print('00前')
else:
    print('00后')
    */
"""
#if 判断3

"""
-------------练习-------------
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖

"""

height = 1.75
weight = 80.5
bmi = int(weight / (height * height))
print("bmi:",bmi)
if bmi > 32:
    print("严重肥胖")
elif bmi > 28 and bmi <= 32:
    print("肥胖")
elif bmi >25 and bmi <= 28:
    print("过重")
elif bmi > 18.5 and bmi <  25:
    print("正常")
else:
    print("过轻")




