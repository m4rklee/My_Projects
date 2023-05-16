from driver_init import driver
from selenium.webdriver.common.by import By
import time
import json
# 使用 mongodb 数据库保存
import pymongo
# 使用 excel 文档保存
import xlwt


# 遍历所有的 url，爬取评论
def spider():
    for url in urls:
        driver.get(url)
        try:
            while driver.find_element(By.CLASS_NAME, 'a-last').is_enabled():
                get_reviews(save_method)
                driver.find_element(By.CSS_SELECTOR, "[class='a-last']").click()
                time.sleep(3)
        except:
            get_reviews(save_method)

# 爬取评论
# 目前只爬取评论中的文本部分，且不含评论的小标题
def get_reviews(method):
    global number
    all_reviews = driver.find_elements(By.CLASS_NAME, 'review-text')
    for rev in all_reviews:
        # 保存到文本文档
        if method == 'txt':
            f.write('\t' + str(number) + '. ')
            f.write(rev.text)
            f.write('\n')
        # 保存到 excel 文件
        elif method == 'excel':
            sheet.write(number - 1, 0, rev.text)
        # 保存到 mongodb 数据库
        elif method == 'mongodb':
            info = {
                "num": number,
                "content": rev.text
            }
            review_collections.insert_one(info)
        else:
            print("请选择正确的保存方式")
            exit(1)

        # 评论计数
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

# 评论计数器
number = 1

# 选择保存方式
save_method = input('请输入保存方式（txt, excel, mongodb)：')
# 保存到文本文档
if save_method == 'txt':
    f = open('reviews.txt', 'w', encoding='utf-8')
    spider()
    f.close()
# 保存到数据库
elif save_method == 'mongodb':
    client = pymongo.MongoClient()
    db = client['REVIEWS']
    review_collections = db.user
    review_collections.drop()
    spider()
    reviews = list(review_collections.find())
    for review in reviews:
        print(review['content'])
# 保存到 excel
elif save_method == 'excel':
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('评论', cell_overwrite_ok=True)
    spider()
    xls.save('评论.xls')
else:
    print("WRONG METHOD")
    exit(1)
