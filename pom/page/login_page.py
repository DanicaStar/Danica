'''
login_page.py
封装页面的表现层
封装页面的操作层
继承base类
'''
from  POM.common.base import Base
login_url=''
class LoginPage(Base):
    '''
    封装表现层：制作定位器
    '''
    username_loc=('id','username')  #用户名输入框
    lopassword_loc = ('id', 'password')  # 密码输入框
    remember_loc=('id','remember')  #记住密码的复选框
    submit_loc=('class name','us_Submit')  #立即登录按钮

    '''
    封装操作层：元素操作
    每一个元素的操作，都写成一个方法
    '''
    #输入用户名
    def input_username(self,text):
        self.send_keys(self.username_loc,text)

    # 输入密码
    def input_password(self, text):
        self.send_keys(self.lopassword_loc, text)

    #点击记住密码
    def click_remember(self):
        if self.is_selected(self.remember_loc)==True:
            pass
        else:
            self.click(self.remember_loc)

    #点击立即登录
    def click_submit(self):
        self.click(self.send_keys())

if __name__ == '__main__':
    from POM.common.base import open_browser
    driver=open_browser()
    login=LoginPage(driver)
    login.open_url(login_url)
    username='Danica'
    password='123'
    login.input_username(username)
    login.input_password(password)
    login.click_remember()
    login.click_submit()



