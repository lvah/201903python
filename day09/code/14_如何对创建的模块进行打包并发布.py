# """
# [kiosk@foundation0 ~]$ mkdir gif^C
# [kiosk@foundation0 ~]$ cd gif
# [kiosk@foundation0 gif]$ cat gif.py
# # ImageSequence: 会将动图分割成每一帧的图片;
# import os
#
# from PIL import  Image, ImageSequence
# def gif_reverse(src_file, dst_file):
#     try:
#             # 打开文件, 并起一个别im
#             with Image.open(src_file) as im:
#                 # 判断图片文件是否为动图?
#                 if im.is_animated:
#                     # 对于图片进行反转
#                     images = [image.copy()  for image in ImageSequence.Iterator(im)][::-1]
#                     # 将反转的图片保存成新的动图;
#                     images[0].save(dst_file, save_all=True, append_images=images[1:])
#
#     except BaseException as e:
#         print("动图反转错误:" , e)
#     else:
#         print("[%s] 反转为 [%s]成功!" %(src_file, dst_file))
#
#
# def gif_split(src_file, dst_dirname):
#     """
#     将gif动图分割为一个个图片
#     :param src_file: 分割的gif文件
#     :param dst_dirname: 存储图片的目录
#     :return:
#     """
#     try:
#         # 打开文件, 并起一个别im
#         with Image.open(src_file) as im:
#             # 判断图片文件是否为动图?
#             if im.is_animated:
#                 # 依次将动图的每个图片保存到文件中;
#                 index = 0
#                 for image in ImageSequence.Iterator(im):
#                     # 获取存储文件的绝对路径;
#                     filename = '%s.png' %(index)
#                     # 为了跨平台, Linux拼接: /, Windows拼接: \   C:\User\python
#                     full_filename = os.path.join(dst_dirname, filename)
#                     image.save(filename)
#                     index += 1
#     except BaseException as e:
#         print("动图分割失败: ", e)
#     else:
#         print("动图分割成功, 保存在[%s]目录中" %(dst_dirname))
#
#
#
# if __name__ == '__main__':
#     gif_reverse('doc/cat.gif', 'doc/cat1.gif')
# [kiosk@foundation0 gif]$
# [kiosk@foundation0 gif]$ cat setup.py
# #从Python发布工具导入"setup"函数
# from distutils.core import setup
#
# setup(
#     name='gif',
#     version='0.0.1',
#     py_modules = ['gif'],
#     author='lvah',
#     author_email='gf_guofan@163.com',
#     url='http://www.lvah.com',
#     description='动图的快速分割与反转'
# )
#
# [kiosk@foundation0 gif]$ python3 setup.py  build^C
# [kiosk@foundation0 gif]$ python3 setup.py sdist^C
# [kiosk@foundation0 gif]$ tree
# .
# ├── build
# │   └── lib
# │       └── gif.py
# ├── dist
# │   ├── gif-0.0.1
# │   │   ├── build
# │   │   │   └── lib
# │   │   │       └── gif.py
# │   │   ├── gif.py
# │   │   ├── PKG-INFO
# │   │   ├── __pycache__
# │   │   │   └── gif.cpython-37.pyc
# │   │   └── setup.py
# │   └── gif-0.0.1.tar.gz
# ├── gif.py
# ├── kiosk@172.25.254.49
# ├── MANIFEST
# └── setup.py
#
# 7 directories, 11 files
# [kiosk@foundation0 gif]$ rm -fr kiosk@172.25.254.49
# [kiosk@foundation0 gif]$ cd dist/
# [kiosk@foundation0 dist]$ tar xf gif-0.0.1.tar.gz ^C
# [kiosk@foundation0 dist]$ python3 setup.py install^C
# [kiosk@foundation0 dist]$ python3
# Python 3.7.1 (default, Dec 14 2018, 19:28:38)
# [GCC 7.3.0] :: Anaconda, Inc. on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import gif
# >>>
# """