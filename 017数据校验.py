import pandas as pd
import matplotlib.pyplot as plt

def score_validation(row):


#读取数据的时候尽量不要设置index，这样可以确保数据都正常列，方便数据校验
students = pd.read_excel('017Students.xlsx')
# print(students)
students.Score