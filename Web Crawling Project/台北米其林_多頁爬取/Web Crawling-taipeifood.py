# 爬取台北市米其林餐廳。
# 網誌規則如下，是否可以用for loop處理翻頁問題
# https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants?sort=distance
# https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants/page/2?sort=distance
# https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants/page/3?sort=distance
# https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants/page/4?sort=distance


# 1.套件
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 處理翻頁的問題->for loop
base_url = 'https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants?sort=distance'
url_formats = {1: 'https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants?sort=distance',
               "other": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants/page/{page_num}?sort=distance"}

start_page = 1
end_page = 5
# 第一頁

url = "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurants?sort=distance"
request_url = requests.get(url)
soup = BeautifulSoup(request_url.text, "lxml")

# 爬取餐廳名
restaurant = soup.find_all('div', class_="col-md-6 col-lg-4 col-xl-3")
restaurant_name = []
for page_num in range(start_page, end_page+1):  # 1-5

    # 處理網址
    if page_num == 1:
        current_url = url_formats[1]
    else:
        current_url = url_formats["other"].format(
            page_num=page_num)  # format格式化。替換字串中的page_num為目前的page_num
    try:
        request_url = requests.get(current_url)
        soup = BeautifulSoup(request_url.text, "lxml")
        restaurant = soup.find_all(
            'div', class_="col-md-6 col-lg-4 col-xl-3")  # 爬取餐廳名

        for name in restaurant:
            title_h3 = name.find("h3", class_="card__menu-content--title")
            if title_h3:
                title_a = title_h3.find("a")
                if title_a:
                    n = title_a.text.strip()
                    restaurant_name.append(n)
                    for title in restaurant_name:
                        print(title)
    # 建議：將您的 except 區塊改成這個樣子
    except requests.exceptions.RequestException as e:
        print(f"頁碼 {page_num} 請求失敗，錯誤原因為: {e}")

df = pd.DataFrame(restaurant_name, columns=["name"])
df.to_csv("Web Crawling-taipeifood.csv", index=False, encoding='utf-8-sig')
