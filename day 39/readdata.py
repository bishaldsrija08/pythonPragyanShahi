import pandas as pd

df = pd.read_csv("./sample_scores.csv")
print(df['score'].max())