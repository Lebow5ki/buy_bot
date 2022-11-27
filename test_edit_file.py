# import pandas as pd
#
#
# r = pd.read_csv('item.csv',sep=';')
# print(r)
# df = pd.DataFrame(r)
# # df = df.drop(columns = ['c_classid'],axis = 1) #Удаляем по названию столбца(axis = 1/0 - столбец/строка)
# df = df.drop(df.columns[[4,5,6,7,8,9,10,11,13,14,15,16]], axis = 1) #Удаляем по номеру столбца (начиная с 0)
# df = df.drop(labels = [1], axis = 0)
# df.to_csv('out.csv',index=False,header=None)
# print(df)
#
#
#
# from datetime import datetime
# from threading import Timer
#
# def on_10th_second():
#     print('yo-ho-ho', datetime.now())
#
#
# def shedule(func, nth_sec):
#     now_sec = datetime.now().second
#     wait = (60 + nth_sec - now_sec) % 60
#
#     Timer(wait, func).start()
#     Timer(wait + 1, lambda: shedule(func, nth_sec)).start()
#
# shedule(request, 10)



import sqlite3

# import pandas as pd
# empdata = pd.read_csv('test.csv', index_col=False, delimiter = ',')
# print(empdata.head())


