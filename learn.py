import pandas as pd
import sys
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv(sys.argv[1])
X = df[["台番号", "前日最終スタート", "date"]]
y = df[["BB回数", "RB回数", "最大差玉", "BB確率", "RB確率"]]
#print(y)
reg = RandomForestRegressor()
reg.fit(X, y)
machine_num = int(sys.argv[2])
last_roll = int(sys.argv[3])
day = int(sys.argv[4])
result = reg.predict([[machine_num, last_roll, day]])
print(result)
result = result.tolist()[0]
bonus_s = result[0:2]
bonus_s = list(map(int, bonus_s))
result[0] = bonus_s[0]
result[1] = bonus_s[1]
result[2] = int(result[2])
print("[BB回数予想  RB回数予想] [BB確率予想  RB確率予想] 合成確率")
merged_percent = (result[3] * result[4]) / ( result[3]+ result[4])
print(result[0:2], f"[1/{result[3]}, ", f"1/{result[4]}]", f"1/{merged_percent}")