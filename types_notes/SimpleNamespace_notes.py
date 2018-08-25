# coding:utf-8
# author: 'lyb'
# Date:2018/8/25 21:42

import types

# SimpleNamespace 一个空类型, class MyClass:pass 可以添加和删除属性

colors = types.SimpleNamespace()

colors.first = "red"

print(colors.first)
print(hasattr(colors, "first"))
del colors.first

print(hasattr(colors, "first"))
