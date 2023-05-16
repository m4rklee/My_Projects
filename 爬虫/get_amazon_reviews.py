from driver_init import driver
from selenium.webdriver.common.by import By
import time
import json

# 爬取评论
# 目前只爬取评论中的文本部分，且不含评论的小标题
def get_reviews(f):
    global number
    reviews = driver.find_elements(By.CLASS_NAME, 'review-text')
    for r in reviews:
        f.write('\t' + str(number) + '. ')
        f.write(r.text)
        f.write('\n')
        number = number + 1

# 待爬取网址
# 目前仅测试了亚马逊中国站点
main_page = 'https://www.amazon.cn/'
urls = [
        # 可以修改为其他商品的评论页面
        'https://www.amazon.cn/product-reviews/B07DJ3DS3V/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
        ]

# 使用cookies登陆亚马逊
driver.get(main_page)
r = open('amazon_cookies.txt', 'r')
cookies = json.load(r)
r.close()
driver.delete_all_cookies()
for c in cookies:
    driver.add_cookie(c)

# 创建文件，保存评论
f = open('reviews.txt', 'w', encoding='utf-8')

# 评论计数
number = 1

# 遍历网址爬取评论
for url in urls:
    driver.get(url)
    try:
        while driver.find_element(By.CLASS_NAME, 'a-last').is_enabled():
            get_reviews(f)
            driver.find_element(By.CSS_SELECTOR, "[class='a-last']").click()
            # 延时可以根据网络状况修改
            time.sleep(3)
    except:
        get_reviews(f)
print('finished')
f.close()
