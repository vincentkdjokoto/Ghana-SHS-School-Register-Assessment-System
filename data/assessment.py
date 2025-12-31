import pandas as pd
from grading import grade

df = pd.read_csv("data/assessments.csv")

df["Total"] = df.iloc[:,2:].sum(axis=1)
df["Grade"] = df["Total"].apply(grade)

df.to_csv("data/final_results.csv", index=False)
print("Assessment processed successfully")
