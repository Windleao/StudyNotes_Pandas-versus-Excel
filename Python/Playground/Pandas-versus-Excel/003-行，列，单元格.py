import  pandas as pd


print('===============================================')
d = {'x':100,'y':200,'z':300} #键值对
print(d.keys())
print(d.values())
print(d['x'])

print('===============================================')
s1 = pd.Series(d)#Series 序列，一串值,和字典很像
print(s1)
print(s1.index)


print('===============================================')
L1 = [100,200,300]
L2 = ['x','y','z']
s2 = pd.Series(L1,index=L2)
print(s2)
print(s2.index)


print('===============================================')
L2 = ['x','y','z']
s3 = pd.Series([100,200,300],index=L2)
print(s3)
print(s3.index)

print('================================================================================')
print('================================================================================')
s4 = pd.Series([1,2,3],index=[1,2,3],name='A')
s5 = pd.Series([10,20,30],index=[1,2,3],name='B')
s6 = pd.Series([100,200,300],index=[1,2,3],name='C')
#df4 = pd.Series({s4.name:s4,s5.name:s5,s6.name:s6})
df4 = pd.DataFrame([s4,s5,s6])
print(df4)

