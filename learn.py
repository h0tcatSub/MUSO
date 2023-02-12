import pandas as pd
import sys
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(sys.argv[1])
X = df[["台番号", "前日最終スタート", "date"]]
y = df[["BB回数", "RB回数", "最大差玉", "BB確率", "RB確率"]]
print(y)
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
print("BB回数", "RB回数", "最大差玉")
print(result[0:3])