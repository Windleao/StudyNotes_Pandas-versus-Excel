import  pandas as pd

# 读取excel文件【people】
people = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_002_People.xlsx')

print(people.shape) #shape 查看出多少行多少列
print(people.columns) #colums 列名是什么
print(people.head(100)) #head(x) 前x条数据，默认为x=5
print('=========================================')
print(people.tail(20)) #tail(n) 前x条数据，默认为n=5
print('Done!')