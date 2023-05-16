from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options.add_argument('user-agent=' + agent)
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
