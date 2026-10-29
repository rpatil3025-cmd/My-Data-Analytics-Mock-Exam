import pandas as pd
#function to calculate average
def calculate_average(marks):
    return sum(marks)/len(marks)
#user input
n=int(input("Enter number of students:"))
names=[]
marks=[]
for i in range(n):
    name=input("Enter name of student:")
    mark=float(input("Enter marks:"))
    names.append(name)
    marks.append(mark)
#create a dataset
df=pd.DataFrame({
    "Name":names,
    "Marks":marks,
})
#conditional statements using function
def result(mark):
    if mark>=75:
        print("Distinction")
    elif mark>=50:
        print("Pass")
    else:
        print("Fail")
        df["Result"]=df["Marks"].apply(result)
#display the dataset
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
#Analysis
print("\nAverage Marks:",calculate_average(marks)) 
print("Highest Marks:",max(marks))  
print("Lowest Marks:",min(marks))   