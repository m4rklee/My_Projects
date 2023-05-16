from selenium.webdriver.common.by import By
from driver_init import driver
import json
import time

url = 'https://www.amazon.cn/'
driver.get(url)
username = input('请输入用户名：')
password = input('请输入密码：')
# 登录
driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a/span').click()
# 账号
driver.find_element(By.CLASS_NAME, 'a-input-text').send_keys(username)
driver.find_element(By.ID, 'ap_legal_agreement_check_box').click()
driver.find_element(By.CLASS_NAME, 'a-button-input').click()
time.sleep(2)

# 密码
driver.find_element(By.CLASS_NAME, 'auth-required-field').send_keys(password)
driver.find_element(By.ID, 'signInSubmit').click()

# 验证码
try:
    driver.find_element(By.CLASS_NAME, 'a-alert-heading')
    driver.find_element(By.ID, 'ap_password').send_keys(password)
    captcha = input('请输入验证码： ')
    driver.find_element(By.ID,'auth-captcha-guess').send_keys(captcha)
    driver.find_element(By.ID, 'signInSubmit').click()
except:
    pass
cookies = driver.get_cookies()
f = open('amazon_cookies.txt', 'w', encoding='utf-8')
f.write(json.dumps(cookies))
f.close()
