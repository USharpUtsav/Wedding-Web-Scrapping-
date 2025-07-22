import pandas as pd
import re

df = pd.read_csv("weddingvenues.csv")
df_sorted = df.sort_values(by="Order", ascending=True)
df_sorted = df_sorted.drop(columns=["Order"])

def clean_phone_number(phone):
    if isinstance(phone, str):
        phone_cleaned = re.sub(r'[^0-9]', '', phone.split(' ext')[0])
        return phone_cleaned
    return ''

df_sorted['C - Phone'] = df_sorted['C - Phone'].apply(lambda x: clean_phone_number(x))

df_sorted.to_csv("weddingvenues_sorted_forsubmission.csv", index=False)
