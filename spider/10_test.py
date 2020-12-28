from selenium import webdriver
import time

url='https://github.com/login'
driver=webdriver.Chrome()
driver.get(url)

user=driver.find_element_by_id('login_field')
username=input("请输入用户名：")
user.send_keys(username)

passwd=driver.find_element_by_id('password')
pwd=input("请输入密码：")
passwd.send_keys(pwd)

time.sleep(3)
button=driver.find_element_by_name('commit')
button.click()

time.sleep(3)
