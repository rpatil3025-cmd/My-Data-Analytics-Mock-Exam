import pandas as pd
def get_dataframe(df_name,columns):
    print(f"\nEnter data for {df_name}(columns:{columns})")
    num_rows=int(input(f"How many rows for {df_name}?"))
    data={col:[] for col in columns}
    for r in range(num_rows):
        print(f"Row {r+1}:")
        for col in columns:
            value=input(f"{col}:").strip()
            if value.isdigit():
                value = int(value)
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            data[col].append(value)
    df = pd.DataFrame(data)
    print(f"\n{df_name}:\n{df}")
    return df
#1.Create Dataset From User Input
print("="*60)
print("STEP1:Build Dataset 1-Student basic info")
print("="*60)
student_df1=get_dataframe("Dataset1(students)",["StudentID","Name","Branch"])
print("STEP2:Build Dataset 2-Student marks")
print("="*60)
marks_df2=get_dataframe("Dataset2(marks)",["StudentID","Marks"])
print("="*60)
print("STEP3:Build Dataset 3-New batch of students(same columns as Dataset1)")
print("="*60)
student_df3=get_dataframe("Dataset3(new students)",["StudentID","Name","Branch"])
#2.Concatenation
combined_students=pd.concat([student_df1,student_df3],axis=0,ignore_index=True)
print("Vertical Concatenation (axis=0):\n",combined_students,"\n")
print("---Enter extra column data to horizontally concatenate with Dataset1---")
n_rows_extra=len(student_df1)
print(f"Must match Dataset1 row count: {n_rows_extra}")
attendance_values=[]
for r in range(n_rows_extra):
    val=input(f"Attendance(%) for row{r+1}:").strip()
    attendance_values.append(int(val) if val.isdigit() else val)
extra_info=pd.DataFrame({"Attendance(%)":attendance_values})
horizontal_concat=pd.concat([student_df1,extra_info],axis=1)
print("Horizontal concatenation (axis=1):\n",horizontal_concat,"\n")
#3.Merge (SQL-style joins based on common key)
inner_merge=pd.merge(student_df1,marks_df2,on='StudentID',how='inner')
print("InnerMerge:\n",inner_merge,"\n")
left_merge=pd.merge(student_df1,marks_df2,on='StudentID',how='left')
print("LeftMerge:\n",left_merge,"\n")
right_merge=pd.merge(student_df1,marks_df2,on='StudentID',how='right')
print("RightMerge:\n",right_merge,"\n")
outer_merge=pd.merge(student_df1,marks_df2,on='StudentID',how='outer')
print("OuterMerge:\n",outer_merge,"\n")
#4.Join Method(join on index instead of column)
df_a=student_df1.set_index('StudentID')
df_b=marks_df2.set_index('StudentID')
joined_df=df_a.join(df_b,how='inner')
print("Join (index-based,inner):\n",joined_df,"\n")
joined_outer_df=df_a.join(df_b,how='outer')
print("Join (index-based,outer):\n",joined_outer_df,"\n")
#5.Merge With Different Column Names
marks_df_renamed=marks_df2.rename(columns={'StudentID':'ID'})
merge_diff_cols = pd.merge(
student_df1,marks_df_renamed,
left_on='StudentID',right_on='ID',
how='inner'
).drop(columns=['ID'])
print("Merge with Different Column Names:\n", merge_diff_cols, "\n") 
#6.Merge On Multiple Keys
print("=" * 60)
print("STEP 4: Build Dataset X - Subjects per semester")
print("=" * 60)
df_x = get_dataframe("Dataset X (Subjects)", ["StudentID", "Semester", "Subject"])
print("=" * 60)
print("STEP 5: Build Dataset Y - Grades per semester")
print("=" * 60)
df_y = get_dataframe("Dataset Y (Grades)", ["StudentID", "Semester", "Grade"])
merge_multi_key = pd.merge(df_x, df_y, on=['StudentID', 'Semester'], how='inner')
print("Merge on Multiple Keys:\n", merge_multi_key, "\n") 