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
cookies = {"af" : "1"}
for i in range(99):
   d_today = datetime.date.today()  # データ取得日
   data_day = d_today - datetime.timedelta(days=i)  # データの日付
   target_url = f"https://daidata.goraggio.com/{sys.argv[1]}/unit_list?hist_num={i}&model={model_name}&ballPrice={sys.argv[2]}&f=1"
   print(target_url) 
   print(session.get(target_url, cookies = cookies))
   break
   #try:
   fetched_dataframes = pd.read_html(target_url, encoding="utf-8")[0]
   print(fetched_dataframes)
   fetched_dataframes["date"] = data_day
   main_data = pd.concat([main_data, fetched_dataframes])
   print(main_data)
   #except:
   #   pass
   time.sleep(random.randint(1, 2))
main_data.reset_index()
print(main_data)
main_data.to_csv('content/main_data.csv')
