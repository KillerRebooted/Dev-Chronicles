import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

#1
print("1.\n")

n1=np.arange(3,13,3.5)
print(n1)
s1=pd.Series(n1)
print(s1)

print()

#2
print("2.\n")

s1=pd.Series({"Jan":31, "Feb":28, "Mar":31})
s1.name="Days"
s1.index.name="month"
print(s1)

print()

#3
print("3.\n")

Ser1=pd.Series([34567,890,450,67892,34777,78902,256711,678291,637632,25723,2367,11789])
print("Top 3 biggest areas are:\n", Ser1.sort_values().tail(3))
print("3 smallest values are:\n", Ser1.sort_values().head(3))

print()

#4
print("4.\n")

n=np.array([1,2,3,4,5,6,7])
d=pd.Series(n)
s1=d[d>=d.quantile(0.75)]
print(s1)

print()

#5
print("5.\n")

s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
print(s.iloc[0])
print(s['c'])
print(s[:3])
print(s[-3:])
print(s[1:5])
print(s[2:-2])

print()

#6
print("6.\n")

dict1 ={'m':1, 'n':2, 'o':3, 'p':'Python'}
dict2 ={'m':5, 'n':6, 'o':7, 'p':8, 'q':9.9}

Data = {'first':dict1, 'second':dict2}
df = pd.DataFrame(Data)
print(df)
Dic2 = {'One':pd.Series([1, 3],index=['a','b']), 'Two':pd.Series([3, 4],index=['a','b'])}
dfseries = pd.DataFrame(Dic2)
print(dfseries)
d1 =[[2, 3, 4], [5, 6, 7],[8, 9, 10]]
d2 =[[2, 4, 8], [1, 3, 9],[11,15,18]]
Data ={'First': d1, 'Second': d2}
df2d = pd.DataFrame(Data)
print(df2d)
dff = pd.DataFrame()
print(dff)

print()

#7
print("7.\n")

dict1={101:'Rahul',102:'Kohli',103:'Dhoni',104:'Yuvi',105:'Sachin',106:'Dravid',
107:'Rohit',108:'Ganguly'}
dict2 ={101:26, 102:31,103:39,104:38,105:45,106:44,107:34,108:44}
dict3 ={101:'Developer',102:'TeamLeader',103:'ProjectHead',104:'Developer',
105:'Manager',106:'Tester',107:'Designer',108:'COE'}
dict4 ={101:17500, 102:27500,103:48500,104:18500,105:45000,106:35000, 107:20500,108:75500}
Data = {'Name':dict1, 'Age':dict2, 'Role':dict3,'Salary':dict4}
df = pd.DataFrame(Data)
print(df,'\n')
df.index.name='Roll_No'
print(f'''{df.head()}
{df.tail()}
{df.head(2)}
{df.tail(1)}''')

print()

#8
print("8.\n")

TNS=np.array([200,180,175,188,196,180,181,191,178,180,200,200])
TNSP=np.array([200,180,174,186,196,180,180,191,178,180,199,200])
PP=TNSP/TNS
d={'Class':['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII'],
'Total_No.of_Stud_Appear':[200,180,175,188,196,180,181,191,178,180,200,200],
'Total_No.of_Stud_Pass':[200,180,174,186,196,180,180,191,178,180,199,200], 'Pass_%':PP*100}
Result=pd.DataFrame(d)
print(Result)
print(Result.dtypes)
print('Shapes of the DataFrame is : ')
print(Result.shape)

print()

#9
print("9.\n")

d={'Category':['TV','Mobile','Washing Machine','AC'],
'Name':['Sony','OnePlus','Whirlpool','Daikin'],
'Exp':[55000,38000,18000,50000]}
quartsales=pd.DataFrame(d, columns=['Category','Name','Exp'])
print(quartsales)
q=quartsales.groupby('Category')
print(q['Exp'].sum())

print()

#10
print("10.\n")

df1 = pd.DataFrame({'mark1':[30,40,15,40],
'mark2':[20,45,30,70]})
df2 = pd.DataFrame({'mark1':[10,20,20,50],
'mark2':[15,25,30,30]})
print(df1)
print(df2)
print(df1.add(df2))
print(df1.subtract(df2))
df1.rename(columns={'mark1':'marks1'}, inplace=True)
print(df1)
df1.rename(index = {0: "zero", 1:"one"}, inplace = True)
print(df1)

print()

#11
print("11.\n")

student = {"unit test": [5, 6, 8, 3, 10], "Unit Test-2": [7, 8, 9, 6, 15]}
student1 = {"unit test": [3, 3, 6, 6, 8], "Unit Test-2": [5, 9, 8, 10, 5]}
ds = pd.DataFrame(student)
ds1 = pd.DataFrame(student1)
print(ds)
print(ds1)
print(ds.sub(ds1))
print(ds.add(ds1))
print(ds.mul(ds1))
print(ds.div(ds1))

print()

#12
print("12.\n")

Student = {"RollNo":[1,2,3,4,5,6], "StudName":["Teena", "Rinku", "Payal", "Akshay", "Garvit", "Yogesh"], "Marks":[90,78,88,89,77,97], "Class":["11A", "11B", "11C", "11A", "11D", "11E"]}

df = pd.DataFrame(Student)

df.to_csv(f"{cur_dir}\\Files\\Student1.csv")

print()

#13
print("13.\n")

d = {'Fridge':[12], 'Cooker':[5], 'Juicer':[15], 'Iron':[11]}
df = pd.DataFrame(d)
print(df)
df.to_csv(f"{cur_dir}\\Files\\file.csv")

print()

#14
print("14.\n")

student=pd.read_csv(f"{cur_dir}/Files/Student.csv", sep=",")
print(student)
student['Science']=[23,56,45,26,63]
student=student.rename({'Name':'Student_Name'},axis='columns')
student=student.drop('English',axis=1)
print(student)

print()

#15
print("15.\n")

sales=pd.read_csv(f"{cur_dir}/Files//Sales.csv",sep=",")
print(sales)
sales['Sales_2020']=[10000,20000,10000,50000,60000]
sales=sales.rename({'Name':'Salesperson'},axis='columns')
sales=sales.drop('Sales_2017',axis=1)
print(sales.head(2))

print()

#16
print("16.\n")

Year = [2000,2004,2005,2006,2008,2010,2012,2014,2015,2016,2018,2020]
Salary= [10000,14000,18000,20000,24000,28000,30000,34000,38000,40000,44000,48000]
plt.plot(Year,Salary,label= 'Salary',)
plt.xlabel ('Years')
plt.ylabel ('Salary')
plt.title('Salary Hike of an Employee')

plt.show()

print()

#17
print("17.\n")

year=[1960,1970,1980,1990,2000,2010]
popul_pakistan=[44.91,58.09,78.07,107.7,138.5,170.6]
popul_india=[449.48,553.57,696.783,870.133,1000.4,1309.1]
plt.plot(year,popul_pakistan,color='green')
plt.plot(year,popul_india,color='orange')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('India v/s Pakistan Population till 2010')
plt.show()

print()

#18
print("18.\n")

Overs = ['1-10','11-20','21-30','31-40','41-50']
Runs= [50,60,55,65,100]
plt.bar(Overs,Runs)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Runs Scored by India')
plt.show()

print()

#19
print("19.\n")

objects=('Dotnet','C++','Java','Python','C','CGI/PERL')
y_pos=np.arange(len(objects))
performance=[8,10,9,20,4,1]
plt.bar(y_pos,performance,align='center',color='blue')
plt.xticks(y_pos,objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()

print()

#20
print("20.\n")

m = [113,85,90,150,149,88,93,115,135,80,77,82,129]
w = [67,98,89,120,133,150,84,69,89,79,120,112,100]
plt.xlabel("sugar range")
plt.ylabel("Total no. of patients")
plt.title("Blood sugar analysis")
plt.hist([m, w], bins=[80,100,125,150], rwidth=0.95, color=["green", "orange"], label=["men", "women"])
plt.legend()
plt.show()

print()

#21
print("21.\n")

Subject=['Maths','Phy.','Chem.','Bio.','C.Sc.','English','Tamil','Hindi']
Class=['XI','XII']
Sub_Percentage=[86,84,78,86,94,87,90,88]
Class_Percentage=[90,100]
plt.bar(Subject,Sub_Percentage,align='center')
plt.bar(Class,Class_Percentage)
plt.xlabel('Subject & Class Names', fontsize=18)
plt.ylabel('Pass Percentage', fontsize=18)
plt.title('Student Result Analysis',fontsize=22)
plt.show()

print()

#22
print("22.\n")

data = pd.read_csv(f"{cur_dir}\\Files\\Tesla_Stock_Data.csv")

plt.plot(data["Date"][::6], data["Close"][::6])
plt.xlabel("Dates")
plt.ylabel("Price (in $)")
plt.title("Tesla Stock Prices")
plt.xticks(rotation=70)

plt.show()