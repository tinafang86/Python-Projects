import csv
result = []  # 後續存放成績的空殼
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
