"""
>>> s = "学生管理系统"
>>> help(s.center)

>>> s.center(50)
'                      学生管理系统                      '
>>> s.center(50, '*')
'**********************学生管理系统**********************'
>>> s.center(50, '-')
'----------------------学生管理系统----------------------'
>>> s.ljust(50, '-')
'学生管理系统--------------------------------------------'
>>> s.rjust(50, '-')
'--------------------------------------------学生管理系统'

"""