import pandas as pd
from datetime import date,timedelta

#空行跳过3行
# books = pd.read_excel('C:/Users/roc-pc/Desktop/data analysis/Books.xlsx')
# books = pd.read_excel('C:/Users/roc-pc/Desktop/data analysis/Books.xlsx',skiprows=3)
#空列跳过,即使用C:F列;此时需要填充ID，故先不设置index_col=ID
#默认ID为float直接转int会出错dtype={'ID':int}（Unable to convert column ID to type <class 'int'>）故可以先转为str类型。
books = pd.read_excel('Books.xlsx',skiprows=3,usecols='C:F',index_col=None,dtype={'ID':str,'InStore':str,'Date':str})
# print(books)
# print(type(books['ID']))
# books['ID'].at[0]=100

# print(books.index) # RangeIndex(start=0, stop=20, step=1)

def add_month(d,md):
    yd = md//12
    m = d.month+md%12
    if m!=12:
        yd+=m//12
        m=m%12
    return date(d.year+yd,m,d.day)

start = date(2018,1,1)
for i in books.index:
    books['ID'].at[i]=i+1
    books.at[i,'ID']=i+1
    books['InStore'].at[i]='Yes' if i%2==0 else 'No'
    #注意日期dtype必须为string,加日期,加天
    # books['Date'].at[i]=start+timedelta(days=i)
    #加年
    # books['Date'].at[i] = date(start.year+i,start.month,start.day)

    #加月份比较难
    books['Date'].at[i] = add_month(start,i)
#
# print(books)
books.set_index('ID',inplace =True)
books.to_excel('Output.xlsx')
print('Done')