# 什么是消息闪现?
消息闪现就是只展示一次的数据/参数.

Flask 提供了一个非常简单的方法来使用闪现系统向用户反馈信息。闪现系统使得在一个请求结束的时候记录一个信息，
然后在且仅仅在下一个请求中访问这个数据。Flask消息闪现可以给用户更好的体验。


# 应用场景
- 上传图片代码，加入消息闪现功能。
- 进入首页只刷一次的广告。
- 用户登录成功的闪现信息。
- 用户登录失败的闪现信息。
- 用户注册成功的闪现信息。
- 用户注册失败的闪现信息。

# 实现步骤

-  先引入一个函数 flash,用于存储你究竟都有哪些信息需要展示
```
from flask import flash 
```

- 使用flash保存,它实际上是暂时帮我们保存在session里面， 存储时需要加密
```
app.config["SECRET_KEY"] = "westos"
```

- Flask后台中存储闪现信息

```
flash("要展示的闪现信息")
```

- 前端页面获取闪现信息

```
{{ get_flashed_messages() }}
```

# 提升篇: 闪现分类
分类闪现，当闪现一个消息时，是可以提供一个分类的。这更符合我们实际开发中的场景，例如，
- 当文件上传成功时，我们提示消息“photo upload success”为绿色；
- 当上传文件失败时，我们提示消息“photo upload error”为红色。

## Flask后台中存储闪现信息
```
flash("photo upload success", "success")
flash("photo upload error", "error")
```


## 前端页面获取闪现信息
```
{% with messages = get_flashed_messages(category_filter=['success'])%}
      {% if messages %}
        <ul>
        {% for message in messages %}
          <li style="color:green">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    
    {% with messages = get_flashed_messages(category_filter=['error'])%}
        {% if messages %}
        <ul>
        {% for message in messages %}
          <li style="color:red">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
```