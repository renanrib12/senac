#%%
import pandas as pd

df=pd.read_csv('ClassicDisco.csv')
print(df.head())
print(df.tail())
# %%
print(df.shape)
# %%
print(df.columns)
# %%
for coluna in df.columns:
    print('coluna',coluna)
# %%
for i,coluna in enumerate(df.columns, start=1):
    print(f'{i}ª coluna: {coluna}')
# %%
print(df[df['Year']>1980])
# %%
print(df[df['Year']>1980][['Year','Track']])
# %%
