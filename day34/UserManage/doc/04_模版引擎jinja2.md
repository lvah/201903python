
# 1. 什么是Jinja2模板引擎?
- 官方网址: http://docs.jinkan.org/docs/jinja2/
Jinja2 是一个现代的，设计者友好的，仿照 Django 模板的 Python 模板语言。 它速度快，被广泛使用，并且提供了可选的沙箱模板执行环境保证安全:
- 1). python的Web开发中， 业务逻辑(实质就是视图函数的内容)和页面逻辑(html件)分开的， 使得代码的可读性增强， 代码容易理解和维护；
- 2). 模板渲染: 在html文件中，通过动态赋值 ，将重新翻译好的html文件(模板引擎生效) 返回给用户的过程。
- 3). 其他的模板引擎: Mako, Template, Jinja2

# 2. Jinja2语法
## Jinja2变量显示语法: 
{{ 变量名 }}
        
##  Jinja2变量内置过滤器:
"hello".lower()
- 完整的过滤器查看位置: http://jinja.pocoo.org/docs/templates/#builtin-filters

```
safe            渲染值时不转义
capitalize      把值的首字母转换成大写,其他字母转换成小写
lower           把值转换成小写形式
upper           把值转换成大写形式
title           把值中每个单词的首字母都转换成大写
trim            把值的首尾空格去掉
striptags       渲染之前把值中所有的 HTML 标签都删掉
```  
     
## 如何自定义过滤器?


## for循环:

```
        {% for i in li%}
            xxx
        {% endfor %}
        
```        
## if语句

```
        {% if user == 'westos'%}
            xxxx
        {% elif user == 'hello' %}
            xxx
        {% else %}
            xxx
        {% endif%}
```
## 宏的操作
- 相当于函数
### 如何定义宏?

```
        <!--相当于python里面的定义函数, 后面使用的场景: 分页显示-->
        {%  macro render(id) %}
            <h1>hello world {{ id }}</h1>
        {% endmacro %}
```
### 如何调用宏?

```
    <!--调用定义好的宏(类似于python中的函数)-->
    {{ render(1) }}
    {{ render(2) }}
    {{ render(3) }}
```
###  include包含操作

- 如何使用: {% include  "06_inclued.html"%}

### 模板的继承: 

一般网站的导航栏和底部不会变化， 为了避免重复编写导航栏信息;
- 如何定义模板?

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}  {% endblock %}</title>
</head>
<body>
<div style="width: 100px; height: 200px" > 这是导航栏</div>
{% block body %}
hello
{% endblock %}
<div style="width: 100px; height: 200px" >这是底部</div>
</body>
</html>
            
```            
- 如何继承基模板?

```
{% extends  '06_base.html'%}
{% block title %}
    继承案例
{% endblock %}
{% block body %}
<span style="color: green">这是最新填的block内容</span>
{% endblock %}
```
