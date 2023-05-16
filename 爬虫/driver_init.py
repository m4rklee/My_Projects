from selenium import webdriver

options = webdriver.ChromeOptions()

# 开启无痕模式
options.add_argument('--incognito')

# 设置 headers 部分
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options.add_argument('user-agent=' + agent)

# 程序运行完毕后是否关闭浏览器，默认为关闭
# options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
