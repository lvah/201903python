import curses

# 接收标准屏幕
def main(stdscr):
    while True:
        # 获取用户的输入;
        action = stdscr.getch()
        if action == curses.KEY_UP:
            stdscr.addstr('up\n')
        elif action == ord('q'):
            exit(0)

curses.wrapper(main)
