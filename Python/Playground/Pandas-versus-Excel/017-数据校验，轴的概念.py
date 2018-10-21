import pandas as pd

'''def score_validation(row):
    try:
        assert 0 <=row.Score<=100
    except:
        print(f'#{row.ID}\tstudent{row.Name} has an invalid score {row.Score}.')'''
def score_validation(row):
    if not 0<=row.Score<=100:
        print(f'#{row.ID}\tstudent{row.Name} has an invalid score {row.Score}.')

students = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_017_Students.xlsx')

students.apply(score_validation,axis=1) #0:从上倒下;1:从左到右
#print(students)


