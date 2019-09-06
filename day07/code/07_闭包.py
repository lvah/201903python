"""

闭包的概念就是当我们在函数内定义一个函数时，这个内部函数使用了外部函数的临时
变量，且外部函数的返回值是内部函数的引用时，我们称之为闭包。
"""

"""
闭包需要满足的三个条件: 
    1. 函数内定义一个函数
    2. 内部函数使用了外部函数的临时变量
    3. 外部函数的返回值是内部函数的引用(指的就是内部的函数名)
"""


def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


# 一元线性方程x+1
line1 = line_conf(1, 1)
# 一元线性方程3x+2
line2 = line_conf(3, 2)
# 一元线性方程4x+3
line3 = line_conf(4, 3)

loopCount = 100
y1 = [line1(item) for item in range(loopCount)]
y2 = [line2(item) for item in range(loopCount)]
y3 = [line3(item) for item in range(loopCount)]

# 图形绘制(pyecharts==0.5.11)===导入绘制折线图的类
from pyecharts import Line

# 创建绘制折线图的对象lineObj
x = list(range(loopCount))  # x轴坐标必须是一个列表;
lineObj = Line(title="一元线性方程图形展示")
lineObj.add(name='y=x+1', x_axis=x, y_axis=y1)
lineObj.add(name='y=3x+2', x_axis=x, y_axis=y2)
lineObj.add(name='y=4x+3', x_axis=x, y_axis=y3)
# 将绘制的图形显示为html文件
lineObj.render('./doc/line.html')
