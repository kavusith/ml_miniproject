
import pandas as pd

df =  pd.read_csv('Student_Marks.csv')



#X AND Y

x = df.drop(columns = ['Marks' ])
y = df['Marks']

#Splitting
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x,y , train_size=0.8)

from sklearn.ensemble import RandomForestRegressor
r = RandomForestRegressor()
r.fit(x_train , y_train)
pre = r.predict(x_test)

#Performance analysis
# from sklearn.metrics import mean_absolute_error
# acc = mean_absolute_error(pre, y_test)
# print(acc)



import pickle

with open('student_marks.pkl' , 'wb') as file:
    pickle.dump(r , file)
