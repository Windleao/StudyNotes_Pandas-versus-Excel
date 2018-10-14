import pandas as pd

#筛选 30≥年龄≥18
def age_18_to_30(a):
    return 18 <= a <=30

#筛选 A级别分数≥85
def level_A(s):
    return 85 <= s <= 100

students = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_008_Students.xlsx',index_col='ID')

#students = students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_A)]
#students = students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_A)]
students = students.loc[students.Age.apply(lambda a:18 <= a <=30)].loc[students.Score.apply(lambda s:85 <= s <= 100)]
print(students)