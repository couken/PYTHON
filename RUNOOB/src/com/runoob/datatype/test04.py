'''
Created on 2018年8月17日

@author: TU
'''
class A:
    pass
class B(A):
    pass

print(isinstance(A(),A))
print(type(A())==A)
print(isinstance(B(),A))
print(type(B())==A)
