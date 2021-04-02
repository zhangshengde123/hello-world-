# #面对对象进阶：对python中的面对对象编程进行更为深入的了解
# #装饰器作用：由于python中熟悉和方法访问权限的问题，虽然我们不建议价格熟悉设置为私有，但是如果直接将属性暴露给外界也是有问题的，不然我们没有办法
# 办法检查赋给熟悉的值是否有效。我们之前的建议是将属性命名已单下划线开头，通过这种方式来按时属性是受保护的，不建议外界直接访问，
# 那么如果想访问属性可以通过属性的getter和setter方法进行对应的操作。如果要做到这段，就可以考虑使用@property包装器来包装getter和setter
# 方法，使得对属性的访问既安全又方便
# class dog(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     #a访问其 getter方法
#     @property
#     def name(self):
#         return self.name
#     @property
#     def age(self):
#         return self.age
#     #修改器 setter方法
#     @age.setter
#     def age(self, age):
#         self.age = age
#
#     def