import pandas as pd

books = pd.read_excel('006Books.xlsx',index_col='ID',)

# books['Price']=books['ListPrice']*books['Discount']

#循环处理:很少用，一般尽量用上面的情况。但是不想从头计算的，用这种方式。
# for i in books.index:
# for i in range(5,16):
#     books['Price'].at[i]=books['ListPrice'].at[i]*books['Discount'].at[i]

#给每本书提高2块钱
#方法一：
#books['ListPrice'] = books['ListPrice']+2
#方法二：
# def add_2(x):
#     return(x+2)
# books['ListPrice'] = books['ListPrice'].apply(add_2)
#比较好的办法用lambda
books['ListPrice'] = books['ListPrice'].apply(lambda x:x+2)

print(books)