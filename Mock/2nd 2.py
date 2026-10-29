import pandas as pd
#function to calculate average
def calculate_average(marks):
    return sum(marks)/len(marks)
#user input
n=int(input("Enter no of students:"))
names=[]
marks=[]
for i in range(n):
    name=input("Enter the student name:")
    mark=float(input("Enter marks:"))
    names.append(name)
    marks.append(mark)
#create dataset
df=pd.DataFrame({
    "Name":names,
    "Marks":marks
})
#conditional statement using function
def result(marks):
    if mark>=75:
        print("Distinction")
    elif mark>=50:
        print("Pass")
    else:
        print("Fail")
        df["Result"]=df["Marks"].apply(result)
#display dataset 
print("\nDataset:")
print(df)
#loop for processing values
print("Student Analysis:")
for mark in marks:
    if mark>=75:
        print("Distinction")
    elif mark>=50:
        print("Pass")
    else:
        print("Fail")
#analysis
print("\nAverage Marks:",calculate_average(marks))
print("Highest Marks:",max(marks))
print("Lowest Marks:",min(marks))