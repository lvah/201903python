# 1. itchat
# 2. 如何获取好友的省份? friend['Province']
# 3. 将来怎么统计对应好友个数; =====defaultdict

sortedFriend = {
    '陕西': 104,
    "山西": 58,
    "山东": 29,
    "四川": 28,
    "河南": 20,
}

# 绘制折线图
from  pyecharts import  Line
# 绘制柱状图
from pyecharts import  Bar

# 创建条形图对象
bar = Bar("好友省份分布")
# 添加条形图绘制的信息
bar.add("", list(sortedFriend.keys()), list(sortedFriend.values()))
# 将绘制的图形保存未html文件, 默认存储于当前目录所再文件render.html
bar.render('doc/province.html')

