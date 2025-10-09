# 安裝套件

import requests  # 爬蟲
from bs4 import BeautifulSoup  # 處理爬蟲資料
import pandas as pd  # 產出csv檔案

# 爬取網址
response = requests.get("https://tmrmds.co/course-introduction-overview/")

# 查看爬取結果，是雜亂的一堆未整理資料
# print(response.text)

# 使用bs4解析HTML/XML，解析爬取成果

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

# 取得特定網站區塊(一個條件.find()/多個條件.find_all())，（找到標籤,提取屬性）
result = soup.find_all('h2', class_='elementor-heading-title')
# print(result)

# 取得標題資料
text = []
for res in result:
    class_name = res.getText()
    # 排除下面字詞
    if class_name not in ["聯絡我們", "服務", "關於臺灣行銷研究", "關注我們"]:
        print(class_name)
        text.append(class_name)

# 取得網址
# 特定要素(.get())，要get什麼、要素名稱 (href是課程入口的要素名).get(提取屬性)
# class_ 保留字，宣告只是參數名稱而非保留字
class_link_element = soup.find_all("a", class_="elementor-button-link")
link = []
for res in class_link_element:
    course_link = res.get("href")
    # 排除聯絡我們
    if course_link not in "https://tmrmds.co/contact_tmr/":
        print(course_link)
        link.append(course_link)

# 取得所有價格
# 所有價格爬取
price = soup.find_all('h4')
price_list = []
for p in price:
    price_num = p.getText()
    print(price_num)
    price_list.append(price_num)

# 爬取課程資訊
# 嘗試抓這一堂"AIGC工程師的第一門課：整合生成式AI系統"
# interested_class = requests.get(
#     "https://courses.taiwanmds.com/product/information?p=9fd5416d7f9b11efb3480242ac110002")
# soup = BeautifulSoup(interested_class.text, "html.parser")

# # 網頁代碼文字化
# class_result = soup.find_all("div", class_="course-main-info-box")
# for c in class_result:
#     span_remove = c.find_all("span")
#     title_remove = c.find_all("h3")
#     for span in span_remove:
#         span.extract()
#     for title in title_remove:
#         title.extract()
#     clean_text = c.getText().replace("\n", "")
#     print(clean_text)

# 爬取每一個課程資訊

post = []
for url in link:
    # 抓取文章
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # 抓取特定網頁區塊
    class_result = soup.find_all("div", class_="course-main-info-box")
    for c in class_result:
        span_remove = c.find_all("span")
        title_remove = c.find_all("h3")
        for span in span_remove:
            span.extract()
        for title in title_remove:
            title.extract()
        clean_text = c.getText().replace("\n", "")
    print(clean_text)
    post.append(clean_text)

# 合併資料集
# zip：迭代打包後面的欄位
all_post = pd.DataFrame(zip(text, link, price_list, post),
                        columns=["標題", "網址", "價格", "課能內容"])
all_post.to_csv("Web Crawling_TMR.csv", index=False, encoding="utf-8-sig")
