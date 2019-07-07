import pandas as pd

# d = {'x':100,'y':200}
# s1 = pd.Series(d)
# print(s1)
# print(s1.index)
# print(s1.data)


# L1 = [100,200,300]
# L2 = ['x','y','z']
# s1 = pd.Series(L1,index=L2)
# print(s1)

s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([100,200,300],index=[1,2,3],name='C')

#把s1,s2,s3当做列加入(最常用)-Dict
df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)
# print('-'*20)
# print(s1)
# print('-'*20)

#把s1,s2,s3按List写入，则是当做行写入
# df = pd.DataFrame([s1,s2,s3])
# print(df)


#index和默认的index是对齐关系，比如修改s3的index不对齐
s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([100,200,300],index=[2,3,4],name='C')

#把s1,s2,s3当做列加入(最常用)-Dict
df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)
'''结果如下：
     A     B      C
1  1.0  10.0    NaN
2  2.0  20.0  100.0
3  3.0  30.0  200.0
4  NaN   NaN  300.0
'''
