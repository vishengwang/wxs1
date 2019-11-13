from time import sleep
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    #打开浏览器
    driver=webdriver.Chrome('../chrome_78/chromedriver.exe')

    #调整窗口大小
    driver.maximize_window()

    #关闭浏览器，而不退出driver
    # driver.close()
    # 打开网址
    yield driver

    driver.quit()#关闭浏览器，退出driver
