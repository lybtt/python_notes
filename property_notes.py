# coding:utf-8
__author__ = 'lyb'
# Date:2018/8/20 19:15
"""
(1) 编写新类时, 应该用简单的public属性来定义其接口, 而不要用手工实现set 和get 方法
(2) 如果访问对象的某个属性时, 需要表现出特殊的行为就用 @property 来定义这种行为
(3) @property 方法需要执行迅速一点, 缓慢或者复杂的工作, 应该放在普通的方法里
(4) @property 可以为现有的实例属性添加新的功能
(5) 可以用 @property 来逐步完善数据模型
(6) @property 用的太过频繁, 那就应该考虑彻底重构该类并修改相关的调用代码
"""


class Song:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        print(f"I'm listening to {(self.title).title()}")    # 3.6 新加的特性 f''

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title.title()


song1 = Song('first song')
song1.show_title()
print(song1.title)
print(song1.__dict__)
song2 = Song('second song')
print(song2.__dict__)
print(song2.title)
song2.title = 'change'
print(song2.title)
print(song2.__dict__)
