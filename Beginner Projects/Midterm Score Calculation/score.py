# 原始成績包含三次作業(50%)和一次期中考（20%）一次期末考(30%)。製作一個計算，作業取2次成績最高的，並計算平均值
# 輸入與輸出皆為csv

# 程式邏輯：讀取檔案->處理計算(計算前2高的成績+期中期末)->讀取新檔案（創建）->寫入規則

result = []  # 後續存放的空殼
with open('/Users/tinafung8686/Desktop/GITHUB/Python-Projects/Beginner Projects/Midterm Score Calculation/學生成績.csv', encoding='big5') as infile:
    reader = csv.reader(infile)  # 建立一個讀取器，它會按行讀取 CSV 檔案，並將每行轉換為字串列表
    # 將讀取器的所有內容（所有行）轉換成一個名為 data_rows 的列表。data_rows[0] 為標頭，data_rows[1:] 為學生資料。
    data_rows = list(reader)  # 把解析結果裝入list

    header = data_rows[0]
    for sco in data_rows[1:]:
        name = sco[0]
        score = [int(sco) for sco in sco[1:]]
        midterm = score[3]
        final_exam = score[-1]
        score_desc = sorted(score, reverse=True)
        hw_avg = (score_desc[0]+score_desc[1]) * 0.5
        final_score = round(midterm * 0.2 + final_exam * 0.3 + hw_avg * 0.5, 2)
        print(name, score, '作業平均', hw_avg, '總分', final_score)
        sco.append(final_score)
        result.append(sco)

with open('/Users/tinafung8686/Desktop/GITHUB/Python-Projects/Beginner Projects/Midterm Score Calculation/學生總成績.csv', 'w', encoding='big5') as outfile:
    header.append('總成績')
    outfile.write(','.join(header) + '\n')
    for stu in result:
        outfile.write(','.join([str(e) for e in stu]) + '\n')


# 成績是數字，當從csv讀取後，數字會變為字串
        # int('123')->123
        # str(123) ->'123'

        # 生程式列表
        # a = [10,20,30]
        # b = [e+1 for e in a]
        # c = [e*2+3 for e in a]
        # print(a, b, c) #[10, 20, 30] [11, 21, 31] [23, 43, 63]

        # x = ['an', 'bo', 'ca']
        # y = [e + 't' for e in x]
        # print(x, y) #['an', 'bo', 'ca'] ['ant', 'bot', 'cat']

# num = [1,2,3,4,5]
# s = sorted(num, reverse=True) #由大到小排序
# print(s)

# for loop example

# lia = '賴賴,90,80'
# chen = '陳陳,70,100'
# data = [lia, chen] # ['賴賴, 90, 80', '陳陳, 70, 100']，先處理lia，再處理chen
# result = []
# for e in data:
#     stu = e.split(',')
#     stu.append(int(stu[2])+1)
#     result.append(stu)

# for stu in result:
#     print(stu)

# #字串合併
# s = '10'
# t = '11'
# u = '12'
# x = s +'/'+ t+'/' + u
# print(x) #10/11/12

# data = [s,t,u]
# y = '/'.join(data) #join把列表裡面的值連接起來
# print(y) #10/11/12
