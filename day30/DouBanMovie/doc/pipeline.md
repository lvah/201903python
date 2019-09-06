
# 1. 管道文件介绍
在项目被蜘蛛抓取后，它被发送到项目管道，它通过顺序执行的几个组件来处理它。
每个项目管道组件（有时称为“Item Pipeline”）是一个实现简单方法的Python类。
他们接收一个项目并对其执行操作，还决定该项目是否应该继续通过流水线或被丢弃并且不再被处理。
# 2. 项目管道的典型用途是：
- 清理HTML数据
- 验证抓取的数据（检查项目是否包含特定字段）
- 检查重复（并删除）
- 将刮取的项目存储在数据库中



# 3. 编写自己的项目管道
每个项目管道组件是一个Python类，必须实现方法：process_item(self, item, spider),参数：
- item（Itemobject或dict） - 剪切的项目
- Spider（Spider对象） - 抓取物品的蜘蛛

对于每个项目管道组件调用此方法。process_item() 必须：
    - 返回一个带数据的dict，返回一个Item （或任何后代类）对象，
    - 返回一个Twisted Deferred或者raise DropItemexception。丢弃的项目不再由其他管道组件处理。


# 4. 额外方法
open_spider(self, spider): 当蜘蛛打开时调用此方法。
close_spider(self, spider): 当蜘蛛关闭时调用此方法。




# 项目一： 处理评分

```
class AddScoreNum(object):
    """在原有评分的基础上加1"""
    def process_item(self, item, spider):
        if item['score']:
            item['score'] += 1
            return item
        else:
            raise DropItem("Missing price in %s" % item)
```


```
class JsonWriterPipeline(object):
    """将所有抓取的项目存储到单个文件中'douban.json'，每行包含一个项目，以JSON格式序列化"""
    def open_spider(self, spider):
        self.file = open('douban.json', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4)
        self.file.write(line)
        return item
```


# 激活项目管道组件

您在此设置中分配给类的整数值确定它们运行的​​顺序：项目从较低值到较高值类。通常将这些数字定义在0-1000范围内。


