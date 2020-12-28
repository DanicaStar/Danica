from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_element(driver,*loc):     #*loc任意多个参数
    e=driver.find_element(*loc)
    return e

if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.maximize_window()
    sleep(1)
    get_element(driver,By.ID,'kw').send_keys('小丸子')    #*loc任意多个参数，这里的  By.ID,'kw'不需要以元组的形式
    # loc=(By.ID,'kw')
    # get_element(driver, *loc).send_keys('小丸子')
    get_element(driver,By.ID,'su').click()
    sleep(3)
    driver.quit()

