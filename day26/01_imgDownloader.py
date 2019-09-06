"""
图片下载器
"""
# -*- coding:utf-8 -*-

import re
import requests
import os
def downloadPic(html, keyword):
    """
    :param html: 页面的源代码
    :param keyword: 搜索的关键字
    :return:
    """
    # (.*?)代表任意多个字符
    # ()代表分组， 值返回符合条件的字符串中括号里面的内容;
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)[:5]
    count = 0
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')

    # each 是每个图片的url地址
    for each in pic_url:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 '
                              'Mobile Safari/537.36'}
            # 获取指定图片的相应对象;
            response = requests.get(each, timeout=10, headers=headers)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        except Exception as e:
            print('【错误】当前图片无法下载')
            print(e)
            continue
        else:
            # print(response.status_code)
            if response.status_code != 200:
                print("访问失败: ", response.status_code)
                continue
        #   ******** 存储图片到本地*******************************
        if not os.path.exists(imgDir):
            print("正在创建目录 ", imgDir)
            os.makedirs(imgDir)

        posix = each.split('.')[-1]
        if posix not in ['png', 'jpg', 'gif', 'jpeg']:
            break
        print('正在下载第' + str(count + 1) + '张图片，图片地址:' + str(each))
        name = keyword + '_' + str(count) + '.' + posix
        filename = os.path.join(imgDir, name)
        count += 1
        with open(filename, 'wb') as f:
            # response.content: 返回的是二进制文本信息
            #  response.text:返回的字符串文本信息
            f.write(response.content)


if __name__ == '__main__':
    imgDir = 'pictures'
    word = input("Input key word: ")
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        content = ''
    else:
        content = response.text

    downloadPic(content, word)
