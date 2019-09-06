from db import  session, User
cookie = {}


class UserManage(object):
    def login(self, name, password):  # name='root', password='123'
        # 如果找到(用户名和密码正确)， 则返回找到的用户对象; 如果没有找到， 返回None;
        obj = session.query(User).filter_by(name=name).filter_by(password=password).first()
        if obj:
            cookie['name'] = name
            print("用户%s登陆成功" %(name))
        else:
            print("用户%s登陆失败" %(name))
          
    def register(self):
        pass

    def logout(self):
        cookie.pop('name')
        print("注销成功.....")

if __name__ == '__main__':
    um = UserManage()
    um.login('westos', '123')