from time import sleep

import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_input(driver):#输入框
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)

    input=driver.find_element_by_xpath("//input[@name='t1']")
    input.clear()#清空
    input.send_keys("我司睡吧")
    sleep(2)


def test_radio(driver):#单选
    driver.get("http://ui.yansl.com/#/radio")#打开浏览器
    sleep(2)

    radio=driver.find_element_by_xpath("//input[@name='sex'][2]")
    #点击
    radio.click()
    sleep(2)


def test_select(driver):#下拉框
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)

    select = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div/input")
    #点击
    select.click()
    sleep(2)
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)



def test_file(driver):#文件  只适用于<input type="file">类文件上传界面入口
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file =driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")
    file.clear()#清空
    file.send_keys("d:\\激活码20190629.txt")
    sleep(2)

def test_file2(driver):  # 文件上传  适用于“点击上传”先在电脑上选择文件 再上传
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button")
    file.click()  # 点击
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(1)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "d:\\激活码20190629.txt")
    sleep(2)
    autoit.control_click("打开", "Button1")
    sleep(2)

def test_alert(driver):#警示框 弹框
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    button =driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")
    button.click()
    sleep(2)
    alert = driver.switch_to.alert#弹框出来后界面都不能动 用switch-to 切换到
    alert.send_keys()
    alert.accept()
    sleep(2)

def test_windows(driver):#windows窗口切换
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    dang_dang = driver.find_element_by_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)#类的实例化 下面可以直接使用里面的方法 相当使用鼠标键盘
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)
        sleep(2)
        if driver.title.__contains__("京东"):
            break

def test_iframe(driver):#嵌套界面
    driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")
    sleep(2)

    frame = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(frame)#切换（switch_to）
    sleep(2)
    driver.find_element_by_partial_link_text('京东').click()
    sleep(2)
    #退出当前iframe
    driver.switch_to.parent_frame()
    #回到初始页面
    #driver.switch_to.default_content()
    sleep(2)
    iframe = driver.find_element_by_xpath("/html/frameset/frameset/frame[2]")
    driver.switch_to.frame(iframe)
    sleep(2)
    inpu = driver.find_element_by_xpath('//*[@id="key"]')
    inpu.send_keys("手机")
    sleep(2)

def test_wait(driver):#
    driver.get("http://ui.yansl.com/#/loading")
    bt = driver.find_element_by_xpath('//*[@id="test_wait"]/span')
    bt.click()
    driver.implicitly_wait(5) # 隐试等待
    bt1 = driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div')

    print(bt1.text)
    sleep(2)

    def test_text(driver):  # 用展示文本做断言
        driver.get("http://ui.yansl.com/#/message")
        buttons = driver.find_element_by_xpath("//label[contains(text(),'自动关闭提示')]/..//span[text()='消息']")
        buttons.click()
        message = driver.find_element_by_xpath("//div[@role='alert']/p")
        text = message.text
        print(text)
        assert "这是一条消息" in text  # 断言
        sleep(2)

    def test_page_soure(driver):  # 对界面原代码做断言
        driver.get("http://ui.yansl.com/")
        driver.find_element_by_xpath("//*[@id='app']/section/section/aside/ul/li[3]/div").click()  # 界面提示 + 点击
        sleep(2)
        driver.find_element_by_xpath("//li[contains(text(),'消息提示')]").click()  # 界面提示 + 点击
        sleep(2)
        source = driver.page_source  # 界面源代码
        print(source)
        assert "手工关闭提示" in source  # 断言
        sleep(2)







