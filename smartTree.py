from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def play():#更改视频播放与暂停
    time.sleep(2)
    above = driver.find_element_by_xpath('//div[@class="videoArea"]')
    ActionChains(driver).move_to_element(above).perform()
    try:
        driver.find_element_by_xpath('//div[@id="playButton"]').click()
    except:
        a=1

def passtime():
    for i in range(6):
        time.sleep(1)
        above = driver.find_element_by_xpath('//div[@class="videoArea"]')
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath('//div[@class="passTime"]').click()

def popup():#弹窗测试关闭
    flag = 1
    time.sleep(3)
    try:
        try:
            driver.find_element_by_xpath('//ul[@class ="topic-list"]/li').click()
        except:
            cc=0
        driver.find_element_by_xpath('//div[@aria-label="弹题测验"]/div/button/i').click()
        flag = 0
        print('存在')
    except:
        print('不存在')
    time.sleep(2)
    return flag


def user():#用户登录
    driver.find_element_by_xpath('//input[@placeholder="请输入手机号"]').send_keys('15280385209')
    driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('CHENlong2464..')
    time.sleep(3)
    driver.find_element_by_xpath('//span[@class="wall-sub-btn"]').click()
    time.sleep(3)

def time_up():#视频时间获取与弹窗检测
    above = driver.find_element_by_xpath('//div[@class="videoArea"]')
    ActionChains(driver).move_to_element(above).perform()
    duration = str(driver.find_element_by_xpath('//span[@class="duration"]').text)
    currenttime = str(driver.find_element_by_xpath('//span[@class="currentTime"]').text)
    time_sum = [i for i in duration.split(':')]
    time_sum = int(time_sum[1]) * 60 + int(time_sum[2])
    time_sum_1 = [i for i in currenttime.split(':')]
    time_sum_1 = int(time_sum_1[1]) * 60 + int(time_sum_1[2])
    time.sleep(2)
    i = 0
    current = -1
    time_sum = time_sum - time_sum_1
    while duration!=currenttime:
        time.sleep(2)
        above = driver.find_element_by_xpath('//div[@class="videoArea"]')
        ActionChains(driver).move_to_element(above).perform()
        duration = str(driver.find_element_by_xpath('//span[@class="duration"]').text)
        currenttime = str(driver.find_element_by_xpath('//span[@class="currentTime"]').text)
        if(current==currenttime):
            if(i<20):
                i+=1
            else:
                time_sum=-1
                break
        print(currenttime,'  ',duration)
        flag = popup()
        if (flag == 0):
            play()
        current = currenttime

    return time_sum

def find_click():#未观看或未观看到100%视频检测与选择
    flag = 1
    for i in range(1,200):
        try:
            driver.find_element_by_xpath('//div[@class="el-scrollbar__view"]/ul[{}]'.format(i))
            print(i-1)
            for j in range(1,200):
                try:
                    driver.find_element_by_xpath('//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]'.format(i,j))
                    print(i - 1, '.', j)
                    try:
                        driver.find_element_by_xpath(
                            '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/li/div/div/b[1]'.format(i, j))
                        try:
                            driver.find_element_by_xpath(
                                '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/li/div/div/b[2]'.format(i, j))
                            print(i, '.', j, ' 已完成')
                        except:
                            driver.find_element_by_xpath(
                                '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/li/div'.format(i, j)).click()
                            flag = 0
                            print('未完成')
                            break
                    except:
                        for k in range(1,200):
                            try:
                                driver.find_element_by_xpath(
                                    '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/ul/li[{}]/div'.format(i,j,k))
                                print(i-1,'.',j,'.',k)
                                try:
                                    driver.find_element_by_xpath(
                                        '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/ul/li[{}]/div/b[2]'.format(i,j,k))
                                    print("已完成")
                                except:
                                    driver.find_element_by_xpath(
                                        '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/ul/li[{}]/div'.format(i,j,k)).click()
                                    time.sleep(5)
                                    flag=0
                                    break
                            except:
                                print("已完成")
                                break

                except:
                    print("已完成")
                    break

                if(flag==0):
                    break
        except:
            print("你已经完成课程\n")
            break
        if(flag==0):
            break

def mains():
    #driver.get("https://studyh5.zhihuishu.com/videoStudy.html#/studyVideo?recruitAndCourseId=4e5c595946524258454a58595e445d43")
    driver.get("https://studyh5.zhihuishu.com/videoStudy.html#/studyVideo?recruitAndCourseId=4e5c595b4c524258454a58595e445e40")
    user()
    flag = popup()
    try:
        driver.find_element_by_xpath('//*[@aria-label="智慧树警告"]/div/button/i').click()
        driver.find_element_by_xpath('//div[@class="el-dialog__header"]/i').click()
    except:
        m=1
    time.sleep(3)
    if(flag==0):
        play()


if __name__=='__main__':
    a = 1
    driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe",options=option)
    driver.maximize_window()
    mains()
    time_sum = 0
    while time_sum <= 2400:
        try:
            above = driver.find_element_by_xpath('//div[@class="videoArea"]')
            ActionChains(driver).move_to_element(above).perform()
            driver.find_element_by_xpath('//div[@class="volumeBox"]').click()
        except:
            print('已经静音')
        if(a<0):
            time.sleep(3)
            driver.refresh()
            play()
        flag = 1
        find_click()
        flag = popup()
        if (flag == 0):
            play()
        time.sleep(3)
        a = time_up()
        time_sum += a
        print("已播放时间：{}s".format(time_sum))