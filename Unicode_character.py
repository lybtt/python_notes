# coding:utf-8
__author__ = 'lyb'
# Date:2018/8/20 9:21

import unicodedata

# unicodedata 模块提供了对unicode 字符数据库的访问, 并隐式的提供了每个字符的属性

print(unicodedata.lookup('RIGHT SQUARE BRACKET'))   # 根据名字查找字符
print(unicodedata.name(u']'))
print(unicodedata.category(u'A'))
print(unicodedata.category(u']'))
print(unicodedata.name(u'a'))
