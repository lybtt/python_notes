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


# ord chr

print(ord('A'))   # 返回一个字符串的Unicode编码
print(chr(65))

# A-Z
str_a_z = [chr(i+ord("A")) for i in range(26)]
print(str_a_z)
# A-Z 与索引值结合
dict_a_z = dict(zip(str_a_z, range(1, 27)))
print(dict_a_z)
