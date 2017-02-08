#!/usr/bin/env python
# --*-- coding:utf-8 --*--

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x>= 0:
        print(x)
        return x;
    else:
        print(-x)
        return -x;


my_abs(-100)

"""
def  printme(str):
      print("str:",str);
      return;

printme("我要调用用户自定义的函数！")

"""
