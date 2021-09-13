from selenium import webdriver
import time
import random


from config import FILEPATH
from common.libs.ReadFile import get_email_list
from common.libs.UserService import getname
from common.libs.DateHelpler import getbirthdate




#读取邮箱名和邮箱密码列表
_, useremail_list, userpwd_list = get_email_list(FILEPATH + "useremail.txt")


#读取lastname和firstname
lastname, firstname = getname()

#读取随机生日
yaer, month, day = getbirthdate()
print(getbirthdate())
#启动浏览器

def autofb():
        #打开浏览器
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/reg")

        input = driver.find_element_by_name("lastname")
        input.send_keys(lastname)

        input = driver.find_element_by_name("firstname")
        input.send_keys(firstname)
        
        input = driver.find_element_by_name("reg_email__")
        input.send_keys(useremail_list[0])
        time.sleep(3)
        input = driver.find_element_by_name("reg_email_confirmation__")
        input.send_keys(useremail_list[0])

    
        input = driver.find_element_by_name("reg_passwd__")
        input.send_keys(userpwd_list[0])
            
        input = driver.find_element_by_id("year")
        input.send_keys(random.randint(1905,2010))

        input = driver.find_element_by_id("month")
        input.send_keys(random.randint(1,12))

        input = driver.find_element_by_id("day")
        input.send_keys(random.randint(1,31))

        input = driver.find_element_by_xpath("//input[@value='1']")
        input.click()

        button = driver.find_element_by_name("websubmit")
        button.click()

autofb()









