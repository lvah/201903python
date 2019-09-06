
# 方法1：一定要在__init__.py告诉包包含的模块;
# import  package_a
# print(package_a.module_a1.a1)
# print(package_a.module_a2.a2)

# # 方法2：不需要__init__.py告诉包包含的模块;
# from package_a  import  module_a1
# print(module_a1.a1)
#
# import  package_a.module_a1 as ma1
# print(ma1.a1)


# Why? 可以直接导入a1变量?   __init__.py(from .module_a1 import  a1)
import  package_a
print(package_a.a1)