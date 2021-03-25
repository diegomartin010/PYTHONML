#!/usr/bin/env python3
file_name="test1.xlsx"
sheet=0

import pandas as pd
df = pd.read_excel(io=file_name, sheet_name=sheet)
print(df.columns[0])  # print first 5 rows of the dataframe
