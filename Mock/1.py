import pandas as pd
df=pd.DataFrame({
    "Name":["Rutuja","Khushi","Snehal","Trupti","Sakshi"],
    "Dept":["CSE","AIDS","CSE","AIDS","CSE"],
    "Marks":[95,85,90,80,92]
})
print("Original data:\n",df)
print("\nSubset(Marks>50):\n",df[df["Marks"]>50])
print("\nSorted by marks(Ascending):\n",df.sort_values("Marks"))
print("\nSorted by marks(Desending):\n",df.sort_values("Marks",ascending=False))
print("\nGrouped(Avrage marks by department):\n",df.groupby("Dept")["Marks"].mean())
print("\nMean=",df["Marks"].mean())
print("\nMedian=",df["Marks"].median())
print("mode=")
print(df["Marks"].mode())