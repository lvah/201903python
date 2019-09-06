# 用来处理图片的模块
from PIL import  Image

# 1). 打开要处理的图片文件;
filename = 'turtle.png'
img = Image.open(filename)

# 2). 图片尺寸的缩放,
out = img.resize((50, 50) , Image.ANTIALIAS)  # 带滤镜缩放的处理， 防止图片失真

# 3). 保存处理好的图片对象
out.save('turtle_resize.png')