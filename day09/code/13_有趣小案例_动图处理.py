# ImageSequence: 会将动图分割成每一帧的图片;
import os

from PIL import  Image, ImageSequence
def gif_reverse(src_file, dst_file):
    try:
            # 打开文件, 并起一个别im
            with Image.open(src_file) as im:
                # 判断图片文件是否为动图?
                if im.is_animated:
                    # 对于图片进行反转
                    images = [image.copy()  for image in ImageSequence.Iterator(im)][::-1]
                    # 将反转的图片保存成新的动图;
                    images[0].save(dst_file, save_all=True, append_images=images[1:])

    except BaseException as e:
        print("动图反转错误:" , e)
    else:
        print("[%s] 反转为 [%s]成功!" %(src_file, dst_file))


def gif_split(src_file, dst_dirname):
    """
    将gif动图分割为一个个图片
    :param src_file: 分割的gif文件
    :param dst_dirname: 存储图片的目录
    :return:
    """
    try:
        # 打开文件, 并起一个别im
        with Image.open(src_file) as im:
            # 判断图片文件是否为动图?
            if im.is_animated:
                # 依次将动图的每个图片保存到文件中;
                index = 0
                for image in ImageSequence.Iterator(im):
                    # 获取存储文件的绝对路径;
                    filename = '%s.png' %(index)
                    # 为了跨平台, Linux拼接: /, Windows拼接: \   C:\User\python
                    full_filename = os.path.join(dst_dirname, filename)
                    image.save(filename)
                    index += 1
    except BaseException as e:
        print("动图分割失败: ", e)
    else:
        print("动图分割成功, 保存在[%s]目录中" %(dst_dirname))



if __name__ == '__main__':
    gif_reverse('doc/cat.gif', 'doc/cat1.gif')