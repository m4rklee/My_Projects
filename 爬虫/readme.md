# Python实现的一个简单爬虫程序
## 简介
因为打算在毕业论文中对评论做情感分析，所以编写了这个简单的爬虫程序帮助收集评论

## 安装 

#### 本机运行环境（仅供参考）
- windows 11 专业版 22H2
- python 3.10.11
- selenium 4.9.1

#### 安装依赖
执行以下命令安装 python 依赖
```
pip install selenium
```

## 使用方式
- 运行 get_cookies.py，登录自己的amazon账号，获取cookies，共爬虫程序登录
- 运行 get_amazon_reviews.py，爬取评论
- 对爬取的评论进行后续处理

## 参考
此项目主要参考了清华大学出版社出版，黄永祥著《实战Python网络爬虫》一书

## 其他
本项目目前处于初期阶段，后续会不断完善\
欢迎提交issues
