# Python实现的一个简单爬虫程序
## 简介
因为打算在毕业论文中对评论做情感分析，所以编写了这个简单的爬虫程序帮助收集评论
- `driver_init.py` 对爬虫所用浏览器做初始化设置
- `get_cookies.py` 获取网站的cookies并保存到本地
- `get_amazon_reviews.py` 使用保存好的cookies登录网站，并进行评论爬取
## 安装 

#### 本机运行环境（仅供参考）
- windows 11 专业版 22H2
- python 3.10.11
- selenium 4.9.1

#### 安装依赖
执行以下命令安装 selenium 库
```
pip install selenium
```
执行以下命令安装 pymongo 库（非必须，仅用于数据库保存方式）
```
pip install pymongo
```
执行以下命令安装 xlwt 库（非必须，仅用于 excel 保存方式）
```
pip install xlwt
```

## 使用方式
- 安装 Python
- 安装所需依赖
- 运行 `get_cookies.py`，保存cookies
- 运行 `get_amazon_reviews.py`，爬取评论
- 对爬取的评论进行后续处理

## 参考
此项目主要参考了清华大学出版社出版，黄永祥著《实战Python网络爬虫》一书

## 其他
本项目目前处于初期阶段，后续会不断完善\
欢迎提交issues
