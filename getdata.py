import datetime
import pandas as pd
import sys
import time
import urllib
import random
import requests

cols = ["台番号", "累計スタート", "BB回数", "RB回数", "ART回数",
        "最大差玉", "BB確率", "RB確率", "ART確率", "合成確率", "前日最終スタート", "date"]
main_data = pd.DataFrame(columns=cols)
model_name = urllib.parse.quote(sys.argv[3])
# for文で99日前までのデータを取得
session = requests.session()
cookies = {"af": "1"}
for i in range(99):
   d_today = datetime.date.today()  # データ取得日
   data_day = d_today - datetime.timedelta(days=i)  # データの日付
   target_url = f"https://daidata.goraggio.com/{sys.argv[1]}/unit_list?hist_num={i}&model={model_name}&ballPrice={sys.argv[2]}&disp=1&graph=1"
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0", "Referer": f"https://daidata.goraggio.com/{sys.argv[1]}/list?mode=psModelNameSearch&bt={sys.argv[2]}&PS=S"}
   # target_url = f"https://daidata.goraggio.com/100862/unit_list?model=%E2%91%A4%EF%BC%B2%EF%BD%85%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E5%A7%8B%E3%82%81%E3%82%8B&ballPrice=5.00&hist_num=8&disp=1&graph=1"
   print(target_url)
   print(session.get(target_url, cookies=cookies, headers = headers).text)
   time.sleep(random.randint(1, 2))
   exit()
   # try:
   fetched_dataframes = pd.read_html(target_url, encoding="utf-8")[0]
   print(fetched_dataframes)
   fetched_dataframes["date"] = data_day
   main_data = pd.concat([main_data, fetched_dataframes])
   print(main_data)
   # except:
   #   pass
   time.sleep(random.randint(1, 2))
main_data.reset_index()
print(main_data)
main_data.to_csv('content/main_data.csv')
