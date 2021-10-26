from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])


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
        if driver.find_element_by_xpath("//div[@class='video-study']/div[8]/div/div[1]/button").is_displayed():
            driver.find_element_by_xpath("//div[@class='video-study']/div[8]/div/div[1]/button").click()
            flag=0
        print("time_sum:", time_sum)
    except:
        cc=0

    try:
        try:
            driver.find_element_by_xpath('//ul[@class ="topic-list"]/li').click()
        except:
            cc=0
        driver.find_element_by_xpath('//div[@aria-label="弹题测验"]/div/button/i').click()
        flag = 0
        print('存在')
    except:
        cc=0
    time.sleep(2)
    return flag

def time_up(k):#视频时间获取与弹窗检测
    time_sum = 0
    currenttime = 0
    time_sum_1 = 0
    while(1):
        try:
            above = driver.find_element_by_xpath('//div[@class="videoArea"]')
            ActionChains(driver).move_to_element(above).perform()
            duration = str(driver.find_element_by_xpath('//span[@class="duration"]').text)
            currenttime = str(driver.find_element_by_xpath('//span[@class="currentTime"]').text)
            time_sum = [i for i in duration.split(':')]
            time_sum = int(time_sum[1]) * 60 + int(time_sum[2])
            time_sum_1 = [i for i in currenttime.split(':')]
            time_sum_1 = int(time_sum_1[1]) * 60 + int(time_sum_1[2])
            time.sleep(2)
            current = -1
            time_sum = time_sum - time_sum_1
            break
        except:
            driver.refresh()

    try:
        t=0
        while duration!=currenttime:
            time.sleep(2)
            above = driver.find_element_by_xpath('//div[@class="videoArea"]')
            ActionChains(driver).move_to_element(above).perform()
            duration = str(driver.find_element_by_xpath('//span[@class="duration"]').text)
            currenttime = str(driver.find_element_by_xpath('//span[@class="currentTime"]').text)
            if(current==currenttime):
                if(k<5):
                    k+=1
                else:
                    return -1
            print(currenttime,'  ',duration)
            flag = popup()
            if (flag == 0):
                play()
            current = currenttime
            t+=1
        return time_sum
    except:
        above = driver.find_element_by_xpath('//div[@class="videoArea"]')
        ActionChains(driver).move_to_element(above).perform()
        currenttime = str(driver.find_element_by_xpath('//span[@class="currentTime"]').text)
        times = [i for i in currenttime.split(':')]
        times = int(times[1]) * 60 + int(times[2])
        driver.refresh()
        return times - time_sum_1

def find_click():#未观看或未观看到100%视频检测与选择
    flag = 1
    for i in range(1,200):
        try:
            driver.find_element_by_xpath('//div[@class="el-scrollbar__view"]/ul[{}]'.format(i))
            for j in range(1,200):
                try:
                    driver.find_element_by_xpath('//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]'.format(i,j))
                    try:
                        driver.find_element_by_xpath(
                            '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/li/div/div/b[1]'.format(i, j))
                        try:
                            driver.find_element_by_xpath(
                                '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/li/div/div/b[2]'.format(i, j))

                        except:
                            driver.find_element_by_xpath(
                                '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/li/div'.format(i, j)).click()
                            flag = 0
                            print(i, '.', j, ' 未完成')
                            break
                    except:
                        for k in range(1,200):
                            try:
                                driver.find_element_by_xpath(
                                    '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/ul/li[{}]/div'.format(i,j,k))

                                try:
                                    driver.find_element_by_xpath(
                                        '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/ul/li[{}]/div/b[2]'.format(i,j,k))
                                except:
                                    driver.find_element_by_xpath(
                                        '//div[@class="el-scrollbar__view"]/ul[{}]/div[{}]/ul/li[{}]/div'.format(i,j,k)).click()
                                    print(i - 1, '.', j, '.', k,' 未完成')
                                    time.sleep(5)
                                    flag=0
                                    break
                            except:
                                break

                except:
                    break

                if(flag==0):
                    break
        except:
            break
        if(flag==0):
            break

def mains(urls):
    username = "15280385209"
    password = "CHENlong2464.."
    driver.get(urls)
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请输入手机号"]')))
    user(username, password)
    flag = popup()
    try:
        driver.find_element_by_xpath('//*[@aria-label="智慧树警告"]/div/button/i').click()
        time.sleep(2)
        driver.find_element_by_xpath('//div[@class="el-dialog__header"]/i').click()
    except:
        m=1
    time.sleep(3)
    if(flag==0):
        play()

def user(username,password):#用户登录
    driver.find_element_by_xpath('//input[@placeholder="请输入手机号"]').send_keys(username)
    driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys(password)
    driver.find_element_by_xpath('//span[@class="wall-sub-btn"]').click()
    WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@aria-label="智慧树警告"]')))
    print("登录成功！！！")

if __name__=='__main__':
    a = 1
    # urls = ["https://studyh5.zhihuishu.com/videoStudy.html#/studyVideo?recruitAndCourseId=425a505846524258454a58595e445945"]
    urls = ["https://studyh5.zhihuishu.com/videoStudy.html#/studyVideo?recruitAndCourseId=425a5e5c46524258454a58595e475147",
            "https://studyh5.zhihuishu.com/videoStudy.html#/studyVideo?recruitAndCourseId=425a505846524258454a58595e445945"]
    #print(str[0])
    for x in range(2):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe",
                                  options=option)
        driver.maximize_window()
        try:
            mains(urls[x])
            time_sum = 0
            error_num = 0
            error_time = 0
            t=0
            while time_sum<= 1600:
                try:
                    i = 0
                    flag = 1
                    find_click()
                    if(a<0):
                        time.sleep(3)
                        driver.refresh()
                        play()
                    flag = popup()
                    if (flag == 0):
                        play()
                    time.sleep(3)
                    try:
                        above = driver.find_element_by_xpath('//div[@class="videoArea"]')
                        ActionChains(driver).move_to_element(above).perform()
                        driver.find_element_by_xpath('//div[@class="volumeBox"]').click()
                    except:
                        print('已经静音')
                    a = time_up(i)
                    time_sum += a
                    print("已播放时间：{}s".format(time_sum))
                    t+=1
                    error_time = time_sum
                except:
                    error_num+=1
                    time_sum = error_time
                    driver.refresh()
                    print(time_sum)

            driver.close()
            print("共发生错误",error_num,"次")
            time.sleep(5)
        except:
            driver.close()
