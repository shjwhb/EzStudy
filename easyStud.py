# while True:
#         phoneNum = input("请输入手机号：")
#         try:
#             passNum = int(phoneNum)
#             if len(str(passNum)) != 11:
#                 print("请输入有效的手机号！")
#                 continue
#             elif len(str(passNum)) == 11:
#                 break
#         except ValueError:
#             print("请输入有效的手机号！")
# passNum = input("请输入密码：")
import subprocess
import sys
pip_mirror = "https://pypi.tuna.tsinghua.edu.cn/simple/"
def importry(name):
        try:
            import name.text
        except ImportError:
            subprocess.check_call(["pip", "install", "-i", pip_mirror, name])
importry("requests")
importry("bs4")
importry("webdriver_manager")
importry("selenium")
importry("keyboard")
# importry("tensorflow")

# import keyboard
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
import random
# import getpass

def get_password():
    print("请输入密码: ", end='', flush=True)  
    password = ""
    
    while True:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:  # 只处理按下的事件
            if event.name == 'enter':  # 检测 Enter 键
                print() 
                break
            elif event.name == 'backspace':  # 检测 Backspace 键
                if password:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)  # 删除最后一个*
            else:
                # 将输入的字符添加到密码中
                password += event.name  
                print('*', end='', flush=True)  # 显示*

                # 阻止输入的字符显示在命令行中
                keyboard.block_key(event.name)

    return password

while True:
    while True:
            phoneNum = input("请输入手机号：")
            try:
                passNum = int(phoneNum)
                if len(str(passNum)) != 11:
                    print("请输入有效的手机号！")
                    continue
                elif len(str(passNum)) == 11:
                    break
            except ValueError:
                print("请输入有效的手机号！")
    passNum = input("请输入密码：")


    chrome_options = Options()

    # 设置日志级别为 SEVERE，抑制无关日志
    chrome_options.add_argument('--log-level=3')  # 0:所有, 1:错误, 2:警告, 3:信息

    # 可选：禁用 GPU 和软件渲染等加速器（可以减少一些日志）
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')


    # import os
    # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    # import tensorflow as tf

    try:
        # pip_mirror = "https://pypi.tuna.tsinghua.edu.cn/simple/"
        # def importry(name):
        #     try:
        #         import name.text
        #     except ImportError:
        #         subprocess.check_call(["pip", "install", "-i", pip_mirror, name])
        # importry("requests")
        # importry("bs4")
        # importry("webdriver_manager")
        # importry("selenium")
        # subprocess.check_call(["pip", "install", "-i", pip_mirror, "requests"])
        # subprocess.check_call(["pip", "install", "-i", pip_mirror, "webdriver_manager"])
        # subprocess.check_call(["pip", "install", "-i", pip_mirror, "bs4"])


        service = Service('chromedriver.exe')
        def getIf():
            iframes = browser.find_elements(By.TAG_NAME, "iframe")
            print(f"Number of iframes: {len(iframes)}")
        def nextIf(iframe = 0,time = 1):
            if time == 1:
                browser.switch_to.frame(iframe)
            elif time > 1:
                for i in range(time):
                    browser.switch_to.frame(0)

        def lastIf(times = 1):
            for i in range(times):
                browser.switch_to.parent_frame()

        # 创建一个 ChromeOptions 对象
        options = webdriver.ChromeOptions()

        # 设置浏览器窗口大小
        options.add_argument("window-size=1920,1080")  # 宽度1280，高度720

        # Set up the Chrome browser
        browser = webdriver.Chrome(options=options,service=service)  # 使用 ChromeOptions 对象创建 Chrome 浏览器实例

        browser.get("https://passport2.chaoxing.com/login?fid=0&refer=http://i.chaoxing.com/")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "phone")))

        # 模拟登录操作
        username = browser.find_element(By.ID, "phone")
        password = browser.find_element(By.ID, "pwd")
        time.sleep(1)

        wait_string = "Loading"

        # 打印初始部分
        print(wait_string, end="", flush=True)

        # 逐个添加点并延迟
        for _ in range(3):  # 可以根据需要调整点的数量
            print(".", end="", flush=True)  # 打印点并不换行
            time.sleep(1)  # 暂停一秒

        print()  # 最后换行


        # 输入用户名和密码
        # print("若出现Created TensorFlow Lite XNNPACK delegate for CPU为正常现象，此时只需要清空输入框重新输入即可")
        # print("若出现[6468:25352:0924/195910.450:ERROR:ssl_client_socket_impl.cc(882)] handshake failed; returned -1, SSL error code 1, net_error -100也为正常现象，你甚至可以只管自己输入即可")
        # while True:
        #     phoneNum = input("请输入手机号：")
        #     try:
        #         passNum = int(phoneNum)
        #         if len(str(passNum)) != 11:
        #             print("请输入有效的手机号！")
        #             continue
        #         elif len(str(passNum)) == 11:
        #             break
        #     except ValueError:
        #         print("请输入有效的手机号！")



        # passNum = input("请输入密码：")
        username.send_keys(phoneNum)

        # passNum = input("请输入密码(输错密码后会在几秒后提示重新输入，别急)：")
        password.send_keys(passNum)
        time.sleep(1)

        # 点击登录
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        # 进入课程页面
        try:
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//h3[@title="课程"]'))).click()
            time.sleep(2)

        except:
            print("密码或手机号错误，请重新输入！")
            password.clear()
            username.clear()        

            continue
        # 切换到军事的 iframe
        nextIf()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "军事理论"))).click()
        time.sleep(2)

        # 切换到作业的 iframe
        for window in browser.window_handles:
            browser.switch_to.window(window)
            if "军事理论" in browser.title:
                break
        # print(browser.title)
        browser.switch_to.frame("frame_content-zj")#和上面一样但是又不一样
        time.sleep(1)

        # 点击“国防的内涵”
        browser.execute_script("document.elementFromPoint(arguments[0], arguments[1]).click();",124 , 260)
        time.sleep(4)


        lastIf()
        nextIf("iframe")
        # nextIf(0,1)
        # getIf()
        # judgment = browser.find_element(By.LINK_TEXT, "任务点已完成")
        # print(judgment)
        # judgment = browser.find_element(By.CLASS_NAME, "left")
        # print(judgment)
        for p in range(1,100,1):
            if p ==1:
                pass
            else:
                nextIf("iframe")

            if browser.find_element(By.ID, "ext-gen1051").get_attribute("aria-label") == "任务点已完成":
                print("看过了下一个")
                lastIf()
                lastIf()

                button = browser.find_element(By.XPATH, "//div[@id='prevNextFocusNext']")
                button.click()
                time.sleep(4)
                # button = browser.find_element(By.XPATH, "//div[@id='prevNextFocusNext']")
                # button.click()
                # time.sleep(5)
                nextIf("iframe")
                try:
                    browser.find_element(By.ID, "ext-gen1050").get_attribute("aria-label") == "任务点已完成" 
                    lastIf()
                    button = browser.find_element(By.XPATH, "//div[@id='prevNextFocusNext']")
                    button.click() 
                    print("题做过了")  
                    time.sleep(3)
                except:
                    print("题没做")
                    lastIf()
                    button = browser.find_element(By.XPATH, "//div[@id='prevNextFocusNext']")
                    button.click()
                    time.sleep(4)
                    button = browser.find_element(By.LINK_TEXT, "下一节")
                    button.click()
                    time.sleep(4)
            else:
                print("没看过")
                # 切换到第一个iframe
                # nextIf()
                # 再次切换到第一个iframe
                nextIf()
                # 查找播放按钮元素
                button = browser.find_element(By.CLASS_NAME, "vjs-big-play-button")
                # 点击播放按钮
                button.click()
                # 等待5秒
                time.sleep(4)

                # 查找视频元素
                video = browser.find_element(By.TAG_NAME, 'video')

                # 获取视频时长
                video_duration = browser.execute_script("return arguments[0].duration;", video)
                currentTime = browser.execute_script("return arguments[0].currentTime;", video)
                # print(f"视频时长: {video_duration}秒")
                print(f"剩余时长: {video_duration - currentTime}秒")

                # 等待视频时长+5秒
                time.sleep(video_duration - currentTime + 10)
                # 切换到父级iframe
                lastIf()
                lastIf()
                button = browser.find_element(By.XPATH, "//div[@id='prevNextFocusNext']")
                button.click()
                time.sleep(4)
                # button = browser.find_element(By.XPATH, "//div[@id='prevNextFocusNext']")
                # button.click()
                # time.sleep(3)
                # button = browser.find_element(By.LINK_TEXT, "下一节")
                # button.click()
                # time.sleep(3)
                nextIf("iframe")
                try:
                    browser.find_element(By.ID, "ext-gen1050").get_attribute("aria-label") == "任务点已完成" 
                    lastIf()
                    button = browser.find_element(By.XPATH, "//div[@id='prevNextFocusNext']")
                    button.click() 
                    print("题做过了")  
                    time.sleep(3)
                except:
                    print("题没做")
                    lastIf()
                    button = browser.find_element(By.XPATH, "//div[@id='prevNextFocusNext']")
                    button.click()
                    time.sleep(3)
                    button = browser.find_element(By.LINK_TEXT, "下一节")
                    button.click()
                    time.sleep(3)
    except:
        print("出错了 ( -.-)( -.-)")
        break