import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus

fake_dataframe = pd.read_csv("CSV\Fake.csv")
real_dataframe = pd.read_csv("CSV\True.csv")

fake_dataframe.info()

print(fake_dataframe.loc[1:5, ["subject"]])


