from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import csv
import time

def write_csv(path, link,code):
    with open(path,'a+') as f:
        csv_write = csv.writer(f)
        data_row = [link,code]
        csv_write.writerow(data_row)


def write_cookies(cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)


driver = webdriver.Chrome('/path/to/your/chromedriver')

with open('resource.csv',newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            driver.get(row['百度云链接'])
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "zbyDdwb")))
                inputBar = driver.find_element_by_id("utjLVR")
                inputBar.send_keys(row['百度提取码'])
                inputBar.submit()
            except:
                pass
            # BDUSS & PTOKEN are essential cookies for free login
            # 这两个cookie在浏览器中登陆后可以查看，然后填写
            # 这些cookies是极其隐秘的信息，泄露这两个cookie就等于泄露了你的百度账户。
            cookies = [
            {'domain':'.baidu.com','path':'/','name':'BDUSS','value':''},
            {'domain':'.passport.baidu.com','path':'/','name':'PTOKEN','value':''}
                    ]
            write_cookies(cookies)

            # 如果有多个文件，勾选“全选”按钮。
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "zbyDdwb")))
                driver.find_elements_by_class_name('zbyDdwb')[0].click()
            # 如果不存在，则空等10秒后继续下面的操作
            except:
                pass

            # 点击“保存到网盘”按钮
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "g-button-blue")))
            save_button = driver.find_elements_by_class_name("g-button-blue")
            save_button[0].click()

            # 点击弹出“确定”按钮，这样会保存到默认的你的网盘的根目录下。
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "g-button-blue-large")))
            save_button1 = driver.find_elements_by_class_name("g-button-blue-large")
            save_button1[0].click()

            driver.delete_all_cookies()
            time.sleep(1)
        except:
            # 如果某个链接保存中出错，将其保存到path指定的csv文件中。
            # 由于未知原因，不能成功保存压缩文件。
            print("error")
            path  = "error_path.csv"
            print(path,row['百度云链接'],row['百度提取码'])
            write_csv(row['百度云链接'],row['百度提取码'])
            continue

        driver.quit()
