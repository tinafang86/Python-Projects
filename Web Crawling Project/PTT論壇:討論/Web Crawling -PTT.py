# 引入套件

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re  # regular expression處理字串

# 爬取PTT資訊版（手機相關）
# 首先要解決一進入時確認滿18歲的頁面，透過cookie over18=1繞過規則，讓我不管怎樣都可以進網站

# 棒球看板
url = "https://www.ptt.cc/bbs/Baseball/index.html"
header = {"cookie": "over18=1"}  # json檔
ptt_tech_url = requests.get(url, headers=header)

# baseball看板首頁解析
soup = BeautifulSoup(ptt_tech_url.text, "lxml")

# 爬取標題

# 確認第一則標題，方便後續寫loop
# [0]取第一則，text:的文字
header_text_1 = soup.find_all('div', class_='title')[0].text
print(header_text_1)

# 所有標題的解析，包含網址與標題
header = soup.find_all('div', class_='title')

# 所有文章標題
title_list = []
for titles in header:
    print(titles.text)  # 只要text的部分
    title_list.append(titles.text)

# 抓取文章對應連結

# 取得header下面的a標籤，a標籤裡面的href內容

# 測試第一則url，方便後面寫loop
title_url_1 = header[0].a["href"]

# for loop取得每一則文章連結
title_url = []
for url in header:
    urls = url.a["href"]
    print(urls)
    # 補足爬取下來網址，前面缺漏的https://....
    title_url.append("https://www.ptt.cc" + urls)


# 爬取文章內容->存入soup
# 爬取第一則網址的內容
topic_01 = requests.get(title_url[0])
soup = BeautifulSoup(topic_01.text, "lxml")

# 抓取content
main_content = soup.find('div', id='main-content')
print(main_content)

# # 抓取作者、版、標題、日期
meta_value_tags = main_content.find_all("span", class_='article-meta-value')
# print(meta_value_tags)

# 命名每一個抓取基本資料
author = meta_value_tags[0].text
board = meta_value_tags[1].text
title = meta_value_tags[2].text
date = meta_value_tags[-1].text

# 爬取文章
content = str(main_content).split('--')[0]  # ptt透過-- 區分文章還是留言
content = content.strip()  # 移除空白

# 開始爬取所有文章
all_articles_data = []

for single_url in title_url:
    response = requests.get(single_url)
    soup = BeautifulSoup(response.text, "lxml")
    main_content = soup.find('div', id='main-content')

    # 爬取文章的基本資訊（作者、標題、日期等）
    meta_value_tags = main_content.find_all(
        "span", class_='article-meta-value')
    author = meta_value_tags[0].text
    board = meta_value_tags[1].text
    title = meta_value_tags[2].text
    date = meta_value_tags[-1].text

    # 爬取文章
    content = str(main_content).split('--')[0]  # ptt透過-- 區分文章還是留言
    content = content.strip()  # 移除空白
    content_soup = BeautifulSoup(content, "lxml")
    content_s = content_soup.get_text(separator="\n", strip=True)

    # 儲存資料
    all_articles_data.append({
        "標題": title,
        "作者": author,
        "日期": date,
        "看板": board,
        "網址": single_url,
        "文字內文": content_s
    })

# 將所有收集到的資料轉換為 Pandas DataFrame
df = pd.DataFrame(all_articles_data)
df.to_csv("Web Crawling-PTT-content.csv", index=False, encoding='utf-8-sig')


# 爬取文章下面的留言
main_content = soup.find('div', id='main-content')
main_content_comment = main_content.find_all('div', class_="push")
# print(main_content_comment)

# 抓取留言資訊
# push-meta_value_tag
# push-userid
# push-content
# push-ipdatetime

tag = main_content_comment[0]
push_type = tag.find("span", class_="push-tag").text.strip()
push_userid = tag.find("span", class_="push-userid").text
push_content = tag.find("span", class_="push-content").text.strip(": ")
push_date = tag.find("span", class_="push-ipdatetime").text.strip(" \n")

comment = []
for c in main_content_comment:
    try:
        # 加入 .strip() 是個好習慣
        push_type = c.find("span", class_="push-tag").text.strip()
        push_userid = c.find("span", class_="push-userid").text
        push_content = c.find("span", class_="push-content").text.strip(": ")
        push_date = c.find("span", class_="push-ipdatetime").text.strip(" \n")
        comment.append([push_type, push_userid, push_content, push_date])
    except AttributeError:
        # 如果任一欄位找不到，就跳過這條推文
        continue

df = pd.DataFrame(comment, columns=["type", "user-id", "content", "date"])
df.to_csv("Web Crawling-PTT-comment.csv", index=False, encoding='utf-8-sig')
