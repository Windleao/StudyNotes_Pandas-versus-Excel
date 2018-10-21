import pandas as pd

students = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_016_Student_Score.xlsx',sheet_name='Students',index_col='ID')
scores = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_016_Student_Score.xlsx',sheet_name='Scores',index_col='ID')

print(students)
print(scores)

print('==================================')
#两表联合
'''table =students.merge(scores,how='left', on='ID').fillna(0)
table.Score = table.Score.astype(int)
print(table)'''

table =students.join(scores,how='left', on='ID').fillna(0)
table.Score = table.Score.astype(int)
print(table)

