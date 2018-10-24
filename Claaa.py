# -*- coding: utf-8 -*-
num=10
class ClassName(object):
        num=1
        def __init__(self):
                print('This is a init func')
                global num #使用global访问全局变量
                num+=10
                print('global num',num)
                self.num+=1
                print('ClassName.num:',self.num)
        def func(self):
                print('ClassName.num:',self.num)

if __name__=='__main__':#模块不导入直接运行，会进入main函数
        c1=ClassName()
        c1.func()