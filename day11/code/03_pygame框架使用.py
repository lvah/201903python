import pygame
import sys
pygame.init()  # 初始化pygame
size = width, height = 320, 240  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            # exit(0) --- 结束程序, 0代表正常退出，
            sys.exit(0)
        # pygame.KEYDOWN： 代表按下键盘
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
            elif event.key == pygame.K_DOWN:
                print('DOWN')
            elif event.key == pygame.K_q: # Q
                sys.exit(0)

pygame.quit()  # 退出pygame


