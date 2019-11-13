from time import sleep

from selenium import webdriver

def test_browser(driver):
    #打开浏览器
    driver = webdriver.Chrome('../chrome_78/chromedriver.exe')
    sleep(1)
    #调整窗口大小
    driver.maximize_window()

    #关闭浏览器，而不退出driver
    # driver.close()
    # 打开网址
    driver.get("http://baidu.com")
    sleep(1)
    #后退
    driver.back()
    #前进
    driver.forward()
    #刷新
    driver.refresh()





#关闭浏览器，不退出driver
    driver.quit()