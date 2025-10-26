# 把每一筆資料轉換為折線圖
# 檔案為csv，成績為hw1, hw2, hw3, ex1, ex2, total
# 順序：匯入套件->處理資料存入list->繪圖

import matplotlib.pyplot as plt
import csv

with open('/Users/tinafung8686/Desktop/GITHUB/Python-Projects/Beginner Projects/Score Curves/學生成績.csv', 'r', encoding='big5') as infile:
    read = csv.reader(infile)
    data_rows = list(read)
    data = []
    header = data_rows[0]
    for sco in data_rows[1:]:  # [tom, 100, 90, 100, 80]...
        name = sco[0]  # 字串
        scores = [float(s) for s in sco[1:]]  # 原本是int儲存但出現error，改為float
        data.append([name] + scores)  # list + list

    for stu in data:
        stu_name = stu[0]
        scores = stu[1:]
        plt.clf()  # 設定全新圖表。如果沒寫這行，歷經每一次for loop的圖會被疊加在同張圖表上
        plt.plot(scores, marker='o')
        # plot參數(a,b)。如果只有一個list，值的預設會是y軸;如果有2個list，a為x軸, b為y軸
        # marker參數：圖例（頂點上面的點點）
        # color參數：線條顏色，可以設定'red', 'blue'等等
        # 線條粗度：linewidth
        plt.title(stu_name)  # title標題
        # ['HW1','HW2','HW3','EX1','EX2','Final'] #xticks[刻度區隔,x軸名稱]
        plt.xticks(range(len(scores)), header[1:])
        plt.xlabel('Items')  # x軸標題
        plt.ylabel('Scores')  # y軸標題
        plt.ylim(0, 110)
        plt.tight_layout()  # 圖表限縮在圖片中
        plt.savefig(stu_name + '.png')  # 儲存格式
        plt.show()


# matplotlib預設狀況下無法顯示中文，因此表格內可先轉換為英文，或下載中文套件
