# 静态文件介绍
动态的 web 应用也需要静态文件，一般是 CSS , 图片和 JavaScript 文件。理想情况下你的 
服务器已经配置好了为你的提供静态文件的服务。


# 静态文件存储位置
在开发过程中， Flask 静态文件位于应用的 /static 目录中。


# 调用方式

```
# 静态文件在文件系统中的位置应该是 static/style.css 。
{{ url_for('static', filename='style.css') }}
```
