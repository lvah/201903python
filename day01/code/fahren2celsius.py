#!/home/kiosk/anaconda3/bin/python
#encoding:utf-8

"""
将华氏温度转换为摄氏温度

"""
fahrenheit = float(input('输入华氏度:'))
#计算摄氏度
celsius = (fahrenheit - 32)/1.8 
print('%.1f华氏度转为摄氏度为%.1f' %(fahrenheit,celsius)) 
