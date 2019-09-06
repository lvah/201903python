# CSS WHAT？


# CSS How？

1. 引入方式(3种):
    1）. 内联式
        <p style="font-size:12px;"></p>
    2). 嵌入式
        <style>
            p{
                font-size:12px;
            }
        </style>
    3). 外联式
        <link rel='stylesheet' type='text/css' href='css/main.css'>


2. CSS选择器
    1). 标签选择器
    2). id选择器    #id名称{样式}
    3). class选择器    .类名称{样式}
    4). 组合选择器    选择器1,  选择器2{   }
    5). 层级选择器:   ul li{ }  ul .page{ }  ul #page{}
    6). 伪选择器:     li:hover{  }  li:after{ }   li.before{ }

3. 比较重要的CSS设置信息
    1). 居中:
        - 块级元素: margin: 0 auto
        - 行内元素: text-aligin: center

    2). 设置显示问题:
        display: inline-block, inline, block

    3). 去掉文本装饰:
        text-decoration: none
        list-display: none

    4). 盒子模型
        paddding: 内边距
        margin:外边距
        border:边框

        paddding-top:
        paddding-bottom:

        padding: 0px 2px 3px 9px; (上， 右， 下， 左)
        padding: 0px 2px, 3px(上, 左右, 下)
        padding: 0px 2px(上下, 左右)

    5). 浮动:
        设置浮动: float:right|left;
        取消浮动: clear:right|left|both;

    6). overflow: hidden;scroll;auto;