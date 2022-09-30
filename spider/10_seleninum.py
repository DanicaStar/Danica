from selenium import webdriver
import time

url='https://xiaoke.kaikeba.com/example/wordpress/'
driver=webdriver.Chrome()
driver.get(url)

title=driver.find_element_by_class_name('entry-title').find_element_by_tag_name('a')
title.click()

link_login=driver.find_element_by_class_name('must-log-in').find_element_by_tag_name('a')
link_login.click()
time.sleep(3)
user=driver.find_element_by_id('user_login')
user.send_keys('kaikeba')

passwd=driver.find_element_by_id('user_pass')
passwd.send_keys('kaikeba888')
time.sleep(3)
button=driver.find_element_by_id('wp-submit')
button.click()

comment=driver.find_element_by_id('comment')
comment.send_keys("小丸子的小丸子")
time.sleep(3)
comment_submit=driver.find_element_by_id('submit')
comment_submit.click()

time.sleep(3)
driver.quit()
