
import pandas as pd
df = pd.read_csv('D:\Trabalho.csv',  delimitert=';' ,  low_memory=False)

df = df.loc[:, 
    [
        "DATA_TOA", 
        "CIDADES", 
        "STATUS", 
        "STATUS SERVICO", 
        "TIPO DE SERVICO" , 
        "TIPO RESIDENCIA",
        "VALOR EMPRESA"
    ]
]

for i in df.columns:
    print(f"\n===== (i) =====")
    print(df[i].value_counts(dropna=False))

df.dropna(subset=['CIDADES'], inplace=True)

df["TIPO RESIDENCIA"] = df["TIPO RESIDENCIA"].replace("Casa", "CASA")

df.to_csv("Trabalho_tratado.csv", index=False, sep=';', encoding="utf-8-sig")
print("Arquivo CSV salvo com sucesso!") 
